FROM python:3.8-slim AS virtualenv-image

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.8-slim AS build-image

COPY --from=virtualenv-image /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
