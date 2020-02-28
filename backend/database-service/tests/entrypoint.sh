#! /bin/bash

HOST=${1:-api}
PORT=${2:-8080}

wait-for-it $HOST:$PORT -t 60 -s -- pytest -ra --junitxml=test-reports/test-report.xml -vv --hasura-endpoint http://$HOST:$PORT