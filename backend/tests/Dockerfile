FROM hasura/graphql-engine:v1.0.0.cli-migrations AS app

WORKDIR /app

FROM python:3.8-slim AS build

RUN apt update && apt install -y gcc wget \
  && wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/local/bin/wait-for-it \
  && chmod u+x /usr/local/bin/wait-for-it

COPY ./backend/tests/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.8-slim AS integration-test

COPY --from=build /usr/local/bin/wait-for-it /usr/local/bin/wait-for-it
COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
COPY --from=app /bin/hasura-cli /usr/local/bin/hasura

WORKDIR /app

COPY ./backend/tests .
COPY ./backend/test-utils ./common_utils
COPY ./shared/fixtures ./fixtures
COPY ./shared/graphql ./fixtures/graphql/calls