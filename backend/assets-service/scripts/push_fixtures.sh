#! /bin/bash

MINIO_ALIAS=${1:-minio}

for category in `ls ../shared/pictures`; do
  mc mb ${MINIO_ALIAS}/$category
  for f in `ls ../shared/pictures/$category/*` ; do
    mc -q cp $f ${MINIO_ALIAS}/$category/$(basename $f)
  done
done