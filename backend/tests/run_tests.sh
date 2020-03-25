#! /bin/bash

if [ "$#" -ne "2" ] ; then
  echo "Usage: $0 <endpoint> <root-dir>"
  echo "Example: $0 http://graphql-engine:8080 /app"
  exit 1
fi

ENDPOINT=$1
ROOT_DIR=$2
TIMEOUT=60

for i in `seq 1 $TIMEOUT`; do
  echo "Trying $i / $TIMEOUT"
  hasura migrate apply --endpoint="$ENDPOINT" --project=${ROOT_DIR}/shared/fixtures/database --up all --skip-update-check
  [ "$?" == "0" ] && break || sleep 2
done
pytest -p no:cacheprovider -ra --junitxml=${ROOT_DIR}/backend/tests/test-reports/test-report.xml -vv --hasura-endpoint="$ENDPOINT" --fixtures-folder="${ROOT_DIR}/shared/fixtures" --graphql-responses-folder="${ROOT_DIR}/shared/fixtures/graphql" --graphql-calls-folder="${ROOT_DIR}/shared/graphql" ${ROOT_DIR}/backend/tests
hasura migrate apply --endpoint="$ENDPOINT" --project=${ROOT_DIR}/shared/fixtures/database --down $(ls ${ROOT_DIR}/shared/fixtures/database/migrations/*.up.sql | wc -l) --skip-update-check
