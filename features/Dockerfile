FROM python:3.8-slim AS features-tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app