#! /bin/bash

if [ $# -ne 1 ] ; then
    echo "Usage: $0 path-to-migrations-folder"
    echo "Example: $0 ./database-service/migrations"
    exit 1
fi

MIGRATIONS_FOLDER=$1

for dir in `ls ${MIGRATIONS_FOLDER}`; do
    mv ${MIGRATIONS_FOLDER}/$dir/down.yaml ${MIGRATIONS_FOLDER}/$dir.down.yaml
    mv ${MIGRATIONS_FOLDER}/$dir/up.yaml ${MIGRATIONS_FOLDER}/$dir.up.yaml
    rm -Rf ${MIGRATIONS_FOLDER}/$dir
done