FROM python:3.8-slim AS builder

COPY ./fixtures-generator/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

FROM python:3.8-slim AS app

WORKDIR /app

COPY ./test-utils ./test_utils
COPY ./fixtures-generator .

RUN chmod u+x entrypoint.sh

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
