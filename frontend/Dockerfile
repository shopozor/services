FROM node:12.10.0-slim AS unit-tests

WORKDIR /app

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
