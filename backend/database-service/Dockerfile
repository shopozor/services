FROM hasura/graphql-engine:v1.0.0-beta.9.cli-migrations AS app

COPY migrations /app/migrations
COPY config.yaml /app

WORKDIR /app