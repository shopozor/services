#! /bin/bash

hasura migrate apply --project ./demo --skip-update-check

for f in `ls ./demo/pics/*` ; do
  mc cp $f minio/people/$(basename $f)
done