#! /bin/bash

HASURA_GRAPHQL_MIGRATIONS_SERVER_TIMEOUT=60
HOST=${1:-graphql-engine}
PORT=${2:-8080}

wait_for_port() {
    log "waiting $HASURA_GRAPHQL_MIGRATIONS_SERVER_TIMEOUT for $PORT to be ready"
    for i in `seq 1 $HASURA_GRAPHQL_MIGRATIONS_SERVER_TIMEOUT`;
    do
        nc -z $HOST $PORT > /dev/null 2>&1 && log "port $PORT is ready" && return
        sleep 1
    done
    log "failed waiting for $PORT" && exit 1
}

wait_for_port