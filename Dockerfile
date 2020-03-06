FROM bitnami/minio-client AS assets-client

WORKDIR /app

COPY ./shared/pictures /app

FROM hasura/graphql-engine:v1.0.0.cli-migrations AS hasura-migrations

# /hasura-migrations is the default folder where the client will look for migrations to apply
COPY ./backend/database-service/migrations /hasura-migrations

WORKDIR /hasura-migrations

FROM python:3.8-slim AS hasura-build

COPY ./backend/database-service/tests/requirements.txt .

RUN apt update && apt install -y wget \
  && wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/local/bin/wait-for-it \
  && chmod u+x /usr/local/bin/wait-for-it \
  && pip install --no-cache-dir -r requirements.txt

FROM python:3.8-slim AS hasura-test

COPY --from=hasura-build /usr/local/bin/wait-for-it /usr/local/bin/wait-for-it
COPY --from=hasura-build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=hasura-build /usr/local/bin /usr/local/bin
COPY --from=hasura-migrations /bin/hasura-cli /usr/local/bin/hasura

WORKDIR /app

COPY ./backend/database-service .
COPY ./backend/test-utils ./utils
COPY ./shared/fixtures ./fixtures

FROM python:3.8-slim AS fixtures-app-builder

COPY ./backend/fixtures-generator/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

FROM python:3.8-slim AS fixtures-app

WORKDIR /app

COPY ./backend/test-utils ./test_utils
COPY ./backend/fixtures-generator .
COPY ./shared/pictures ./pictures

RUN chmod a+x entrypoint.sh

COPY --from=fixtures-app-builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=fixtures-app-builder /usr/local/bin /usr/local/bin
COPY --from=hasura-migrations /bin/hasura-cli /usr/local/bin/hasura

FROM python:3.8-slim AS integration-test-build

RUN apt update && apt install -y gcc wget \
  && wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/local/bin/wait-for-it \
  && chmod u+x /usr/local/bin/wait-for-it

COPY ./backend/tests/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.8-slim AS integration-test

COPY --from=integration-test-build /usr/local/bin/wait-for-it /usr/local/bin/wait-for-it
COPY --from=integration-test-build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=integration-test-build /usr/local/bin /usr/local/bin
COPY --from=hasura-migrations /bin/hasura-cli /usr/local/bin/hasura

WORKDIR /app

COPY ./backend/tests .
COPY ./backend/test-utils ./common_utils
COPY ./shared/fixtures ./fixtures
COPY ./shared/graphql ./fixtures/graphql/calls

FROM cypress/base:12.13.0 AS cypress-tests

ENV CI=1
ENV CYPRESS_CACHE_FOLDER /home/node/.cache/Cypress
ARG CYPRESS_VERSION="3.7.0"
RUN npm config -g set user $(whoami)
RUN npm install -g "cypress@${CYPRESS_VERSION}" lerna
RUN cypress verify
RUN cypress cache path
RUN cypress cache list
WORKDIR /app

FROM node:13.8.0-alpine AS node-dependencies

WORKDIR /app
COPY ./lerna.json .
COPY ./package.json .
COPY ./yarn.lock .
COPY ./frontend/admin-ui/package.json ./frontend/admin-ui/package.json
COPY ./frontend/admin-ui/yarn.lock ./frontend/admin-ui/yarn.lock
COPY ./frontend/consumer-ui/package.json ./frontend/consumer-ui/package.json
COPY ./frontend/consumer-ui/yarn.lock ./frontend/consumer-ui/yarn.lock
RUN yarn \
  && npx lerna bootstrap \
  && npx lerna exec yarn --concurrency 1

COPY ./frontend/admin-ui ./frontend/admin-ui
COPY ./frontend/consumer-ui ./frontend/consumer-ui
COPY ./shared ./shared
COPY .eslintrc.js .eslintrc.js

FROM node-dependencies AS jest-unit-testing

WORKDIR /app

CMD [ "yarn", "test:unit:ci" ]

FROM node-dependencies AS node-builder

ARG ASSETS_API
WORKDIR /app
RUN npx lerna run build-storybook --concurrency 1

FROM nginx:1.16.0 AS admin-storybook

COPY --from=node-builder /app/frontend/admin-ui/storybook-static /srv

FROM nginx:1.16.0 AS consumer-storybook

COPY --from=node-builder /app/frontend/consumer-ui/storybook-static /srv

FROM node-dependencies AS node-app-builder

ARG GRAPHQL_API
ARG ASSETS_API

WORKDIR /app
RUN npx lerna run build --scope admin-ui \
  && npx lerna run build --scope consumer-ui -- --spa

FROM nginx:1.16.0 AS admin-ui

COPY --from=node-app-builder /app/frontend/admin-ui/dist/spa /srv

FROM nginx:1.16.0 AS consumer-ui-spa

COPY --from=node-app-builder /app/frontend/consumer-ui/dist /srv/static