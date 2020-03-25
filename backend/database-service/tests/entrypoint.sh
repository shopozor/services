#! /bin/bash

HOST=${1:-graphql-engine}
PORT=${2:-8080}
ROOT_DIR=${3:-/app}

wait-for-it $HOST:$PORT -t 60 -s -- pytest -p no:cacheprovider --database-service-folder ${ROOT_DIR}/backend/database-service --fixtures-folder ${ROOT_DIR}/shared/fixtures -ra --junitxml=${ROOT_DIR}/backend/database-service/test-reports/test-report.xml -vv --hasura-endpoint http://$HOST:$PORT ${ROOT_DIR}/backend/database-service