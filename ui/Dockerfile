FROM node:12.10.0-slim AS builder

WORKDIR /home/node

COPY ./package.json ./package.json

RUN yarn 

WORKDIR /app

COPY . .

ARG GRAPHQL_API

RUN yarn build --modules-folder /home/node/node_modules

FROM node:12.10.0-slim AS unit-tests

WORKDIR /app

COPY --from=builder /home/node /home/node

FROM cypress/base:12.13.0 AS cypress-tests

WORKDIR /app

COPY --from=builder /home/node /home/node

FROM cypress/base:12.13.0 AS e2e

RUN yarn global add @quasar/cli

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