FROM node:12.10.0-slim AS unit-tests

WORKDIR /app

FROM cypress/base:12.13.0 AS cypress-tests

WORKDIR /app

FROM node:12.10.0-slim AS app

WORKDIR /app
COPY ./package.json ./package.json
COPY ./lerna.json ./lerna.json
COPY ./frontend/ ./frontend/
ARG GRAPHQL_API
RUN yarn global add lerna \
  && yarn \
  && lerna bootstrap \
  && lerna run build
