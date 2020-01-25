#! /bin/bash

MINIO_ALIAS=${1:-minio}

for category in `ls ../shared/pictures`; do
  mc rm --recursive --force ${MINIO_ALIAS}/$category
done