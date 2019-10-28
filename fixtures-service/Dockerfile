FROM python:3.8-slim

COPY requirements.txt /tmp

WORKDIR /tmp

RUN pip install -r requirements.txt \
  && rm requirements.txt

WORKDIR /app