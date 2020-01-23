FROM hasura/graphql-engine:v1.0.0.cli-migrations AS hasura-image

FROM python:3.8-slim AS build

RUN apt-get update && apt-get install -y gcc

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.8-slim AS features-tests

COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
COPY --from=hasura-image /bin/hasura-cli /usr/local/bin/hasura

WORKDIR /app