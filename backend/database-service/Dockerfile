FROM hasura/graphql-engine:v1.0.0.cli-migrations AS app

COPY migrations /app/migrations
COPY config.yaml /app

WORKDIR /app

FROM hasura/graphql-engine:v1.0.0.cli-migrations AS hasura-migrations

# /hasura-migrations is the default folder where the client will look for migrations to apply
COPY migrations /hasura-migrations

WORKDIR /hasura-migrations

FROM python:3.8-slim AS build

COPY tests/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.8-slim AS test

COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
COPY --from=app /bin/hasura-cli /usr/local/bin/hasura

WORKDIR /app
