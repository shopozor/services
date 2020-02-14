#! /bin/bash

MINIO_ALIAS=${1:-minio}

for category in `ls ../shared/pictures`; do
  for f in `ls ../shared/pictures/$category/*` ; do
    mc cp $f ${MINIO_ALIAS}/$category/$(basename $f)
  done
done