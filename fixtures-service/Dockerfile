FROM python:3.8-slim

WORKDIR /tmp

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
  && rm requirements.txt

WORKDIR /app
