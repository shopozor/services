FROM node:12.10.0-slim AS unit-tests

WORKDIR /app

FROM cypress/base:12.13.0 AS cypress-tests

ENV CI=1
ARG CYPRESS_VERSION="3.7.0"

RUN npm config -g set user $(whoami)
RUN npm install -g "cypress@${CYPRESS_VERSION}"
RUN cypress verify

RUN cypress cache path
RUN cypress cache list

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
