FROM hasura/graphql-engine:v1.0.0-beta.9.cli-migrations AS app

COPY migrations /app/migrations
COPY config.yaml /app

WORKDIR /app

FROM python:3.8-slim AS unittest

COPY --from=app /bin/hasura-cli /usr/local/bin/hasura

COPY tests/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app