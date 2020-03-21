#! /bin/bash

HOST=${1:-graphql-engine}
PORT=${2:-8080}
ROOT_DIR=${3:-/app}

cd ${ROOT_DIR}/backend/tests
wait-for-it $HOST:$PORT -t 60 -s -- ${ROOT_DIR}/backend/tests/run_tests.sh http://$HOST:$PORT ${ROOT_DIR}