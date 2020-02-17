FROM node:13.8.0-alpine AS dependencies

WORKDIR /app
COPY ./lerna.json .
COPY ./package.json .
COPY ./yarn.lock .
COPY ./frontend/admin-ui/package.json ./frontend/admin-ui/package.json
COPY ./frontend/admin-ui/yarn.lock ./frontend/admin-ui/yarn.lock
COPY ./frontend/consumer-ui/package.json ./frontend/consumer-ui/package.json
COPY ./frontend/consumer-ui/yarn.lock ./frontend/consumer-ui/yarn.lock
COPY ./backend/site-generator-service/package.json ./backend/site-generator-service/package.json
COPY ./backend/site-generator-service/yarn.lock ./backend/site-generator-service/yarn.lock
RUN yarn \
  && npx lerna bootstrap \
  && npx lerna exec yarn --concurrency 1

COPY ./frontend/admin-ui ./frontend/admin-ui
COPY ./frontend/consumer-ui ./frontend/consumer-ui
COPY ./backend/site-generator-service ./backend/site-generator-service
COPY ./shared ./shared
COPY .eslintrc.js .eslintrc.js

FROM dependencies AS builder

ARG GRAPHQL_API
WORKDIR /app
RUN npx lerna run build --scope admin-ui \
  && npx lerna run build-storybook

FROM nginx:1.16.0 AS admin-ui

COPY --from=builder /app/frontend/admin-ui/dist/spa /srv

FROM nginx:1.16.0 AS admin-storybook

COPY --from=builder /app/frontend/admin-ui/storybook-static /srv

FROM nginx:1.16.0 AS consumer-storybook

COPY --from=builder /app/frontend/consumer-ui/storybook-static /srv

FROM node:13.8.0-alpine AS site-generator

COPY --from=builder /app/frontend/consumer-ui /data/frontend/consumer-ui
COPY --from=builder /app/shared/graphql /data/shared/graphql
COPY --from=builder /app/backend/site-generator-service /app/

CMD [ "yarn", "start" ]