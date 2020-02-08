FROM python:3.8-slim AS builder

COPY ./backend/fixtures-generator/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

FROM hasura/graphql-engine:v1.0.0.cli-migrations AS hasura-migrations

FROM python:3.8-slim AS app

WORKDIR /app

COPY ./backend/test-utils ./test_utils
COPY ./backend/fixtures-generator .
COPY ./shared/pictures ./pictures

RUN chmod a+x entrypoint.sh

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=hasura-migrations /bin/hasura-cli /usr/local/bin/hasura
