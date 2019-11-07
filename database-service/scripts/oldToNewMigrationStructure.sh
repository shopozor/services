#! /bin/bash

if [ $# -ne 1 ] ; then
    echo "Usage: $0 path-to-migrations-folder"
    echo "Example: $0 ./database-service/migrations"
    exit 1
fi

MIGRATIONS_FOLDER=$1

cd ${MIGRATIONS_FOLDER}
for file in `ls *.up.yaml`; do
    folder_name=${file%.up.yaml}
    mkdir ${folder_name}
    mv ${folder_name}.down.yaml ${folder_name}/down.yaml
    mv ${folder_name}.up.yaml ${folder_name}/up.yaml
done
cd -