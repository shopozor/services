#! /bin/bash

FIXTURES_SET=${1:-small}
FIXTURES_FOLDER=${2:-./fixtures}
FIXTURES_MIGRATIONS_FOLDER=${3:-${FIXTURES_FOLDER}/migrations}
APP_ROOT=${4:-./}
FIXED_TIMESTAMP=${5:-true}

GENERATE_JSON_FIXTURES=${APP_ROOT}/tests/fixtures-generator/generate_json_fixtures.py
JSON_TO_SQL=${APP_ROOT}/tests/fixtures-generator/json2sql.py

if [ ! -d ${FIXTURES_MIGRATIONS_FOLDER} ]; then mkdir -p ${FIXTURES_MIGRATIONS_FOLDER}; fi

python ${GENERATE_JSON_FIXTURES} -o ${FIXTURES_FOLDER}

# TODO: refactor this!
cd ${APP_ROOT}/migrations
index=$(($(ls | tail -n 1 | cut -d "_" -f 1)+1))
cd -

for persona in consumers producers managers rex softozor; do
    # TODO: refactor this!
    if [ "${FIXED_TIMESTAMP}" == "true" ] ; then
        python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Users/$persona.json -n shopozor-$persona -o ${FIXTURES_MIGRATIONS_FOLDER} -t $index
    else
        python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Users/$persona.json -n shopozor-$persona -o ${FIXTURES_MIGRATIONS_FOLDER}
    fi
    index=$((index+1))
done
if [ "${FIXED_TIMESTAMP}" == "true" ] ; then
    python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Shopozor.json -n shopozor-data -o ${FIXTURES_MIGRATIONS_FOLDER} -t $index
else
    python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Shopozor.json -n shopozor-data -o ${FIXTURES_MIGRATIONS_FOLDER}
fi
# without file config.yaml (even empty), hasura migrate apply will fail
touch ${FIXTURES_FOLDER}/config.yaml