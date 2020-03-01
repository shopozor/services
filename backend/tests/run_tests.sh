#! /bin/bash

if [ "$#" -ne "1" ] ; then
  echo "Usage: $0 <endpoint>"
  echo "Example: $0 http://graphql-engine:8080"
  exit 1
fi

ENDPOINT=$1

hasura migrate apply --endpoint $ENDPOINT --project ./fixtures/database --up all --skip-update-check
pytest -ra --junitxml=test-reports/test-report.xml -vv --hasura-endpoint $ENDPOINT
hasura migrate apply --endpoint $ENDPOINT --project ./fixtures/database --down $(ls ./fixtures/database/migrations/*.up.sql | wc -l) --skip-update-check
