#! /bin/bash

HOST=${1:-graphql-engine}
PORT=${2:-8080}

wait-for-it $HOST:$PORT -t 60 -s -- ./run_tests.sh http://$HOST:$PORT