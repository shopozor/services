
#! /bin/sh

TIMEOUT=60
HOST=${1:-minio}
PORT=${2:-9000}

echo "waiting $TIMEOUT seconds for $PORT to be ready on host $HOST"
for i in `seq 1 $TIMEOUT`;
do
    echo "waiting for minio service"
    mc config host add ${MINIO_ALIAS} ${MINIO_URL} ${MINIO_ACCESS_KEY} ${MINIO_SECRET_KEY}
    [ "$?" == "0" ] && break || sleep 1
done

mc mb ${MINIO_ALIAS}/food
mc policy set public ${MINIO_ALIAS}/food
mc mb ${MINIO_ALIAS}/people
mc policy set public ${MINIO_ALIAS}/people
mc mb ${MINIO_ALIAS}/shops
mc policy set public ${MINIO_ALIAS}/shops
