FROM hasura/graphql-engine:v1.0.0-beta.9.cli-migrations AS app

COPY migrations /app/migrations
COPY config.yaml /app

WORKDIR /app

FROM python:3.8-slim AS unittest

RUN apt-get -y update \
  && apt-get install -y curl \
  && curl -L https://github.com/hasura/graphql-engine/raw/master/cli/get.sh | bash

COPY tests/requirements.txt /tmp

WORKDIR /tmp

RUN pip install -r requirements.txt \
  && rm requirements.txt

WORKDIR /app