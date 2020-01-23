#! /bin/bash

MINIO_ALIAS=${1:-minio}

for category in `ls ../shared/pictures`; do
  mc rb ${MINIO_ALIAS}/$category --force
done