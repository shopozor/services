#! /bin/bash

MINIO_ALIAS=${1:-minio}
MINIO_URL=${2:-http://localhost:9001}
MINIO_ACCESS_KEY=${3:-minio}
MINIO_SECRET_KEY=${4:-minio123}

mc config host add ${MINIO_ALIAS} ${MINIO_URL} ${MINIO_ACCESS_KEY} ${MINIO_SECRET_KEY}
for category in `ls ../shared/pictures`; do
  mc rm --recursive --force ${MINIO_ALIAS}/$category
done