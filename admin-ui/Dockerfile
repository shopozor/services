FROM node:12.10.0-slim AS builder

ENV CYPRESS_CACHE_FOLDER /home/node/.cache/Cypress
WORKDIR /home/node
COPY ./package.json ./package.json
RUN npm config set cache /home/node/.cache \
  && yarn && chown node -R node_modules .cache
WORKDIR /app
COPY . .
ARG GRAPHQL_API
RUN ln -s /home/node/node_modules/ node_modules && yarn build

FROM node:12.10.0-slim AS unit-tests

RUN npm config set cache /home/node/.cache
WORKDIR /app
COPY --from=builder /home/node /home/node

FROM cypress/base:12.13.0 AS cypress-tests

ENV CYPRESS_CACHE_FOLDER /home/node/.cache/Cypress
RUN npm config set cache /home/node/.cache
WORKDIR /app
COPY --from=builder /home/node /home/node

FROM cypress/base:12.13.0 AS e2e

ENV CYPRESS_CACHE_FOLDER /home/node/.cache/Cypress
RUN npm config set cache /home/node/.cache \
  && yarn global add @quasar/cli
WORKDIR /app
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/dist ./dist
COPY --from=builder /home/node /home/node

FROM node:12.10.0-slim AS app

WORKDIR /app
RUN yarn global add @quasar/cli
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/dist ./dist

CMD ["yarn", "start"]