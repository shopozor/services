FROM python:3.8-slim AS builder

COPY ./backend/fixtures-generator/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

FROM python:3.8-slim AS app

WORKDIR /app

COPY ./backend/test-utils ./test_utils
COPY ./backend/fixtures-generator .

RUN chmod a+x entrypoint.sh

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
