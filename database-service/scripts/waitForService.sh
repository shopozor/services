#! /bin/bash

HASURA_GRAPHQL_MIGRATIONS_SERVER_TIMEOUT=60
HOST=${1:-graphql-engine}
PORT=${2:-8080}

wait_for_port() {
    echo "waiting $HASURA_GRAPHQL_MIGRATIONS_SERVER_TIMEOUT for $PORT to be ready on host $HOST"
    for i in `seq 1 $HASURA_GRAPHQL_MIGRATIONS_SERVER_TIMEOUT`;
    do
        echo "waiting for graphql engine"
        nc -z $HOST $PORT > /dev/null 2>&1 && echo "port $PORT is ready on host $HOST" && return
        sleep 1
    done
    echo "failed waiting for $PORT on host $HOST" && exit 1
}

wait_for_port