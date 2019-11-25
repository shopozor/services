FROM node:12.10.0-slim AS builder

WORKDIR /app

COPY . .

ARG GRAPHQL_API

RUN yarn && yarn build

FROM node:12.10.0-slim AS unit-tests

COPY --from=builder /root/.cache /home/node/.cache
RUN chown node -R /home/node/.cache

WORKDIR /app

FROM cypress/base:12.1.0 AS cypress-tests

COPY --from=builder /root/.cache /home/node/.cache
RUN chown node -R /home/node/.cache

WORKDIR /app

FROM cypress/base:12.1.0 AS e2e

WORKDIR /app

RUN yarn global add @quasar/cli

COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/dist ./dist
COPY --from=builder /root/.cache /home/node/.cache
RUN chown node -R /home/node/.cache

FROM node:12.10.0-slim AS app

WORKDIR /app

RUN yarn global add @quasar/cli

COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/dist ./dist

CMD ["yarn", "start"]