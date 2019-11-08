#! /bin/bash

FIXTURES_FOLDER=fixtures
APP_ROOT=.

GENERATE_JSON_FIXTURES=${APP_ROOT}/generate_json_fixtures.py
JSON_TO_SQL=${APP_ROOT}/json2sql.py


# Generate the json fixtures
python ${GENERATE_JSON_FIXTURES} -o ${FIXTURES_FOLDER}

# Generate the sql migrations based on the json fixtures
for FIXTURES_SET in tiny small medium large ; do
    FIXTURES_MIGRATIONS_FOLDER=${FIXTURES_FOLDER}/${FIXTURES_SET}/migrations
    if [ ! -d ${FIXTURES_MIGRATIONS_FOLDER} ]; then mkdir -p ${FIXTURES_MIGRATIONS_FOLDER}; fi
    for persona in consumers producers managers rex softozor; do
        python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Users/$persona.json -n shopozor-$persona -o ${FIXTURES_MIGRATIONS_FOLDER}
    done
    python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Shopozor.json -n shopozor-data -o ${FIXTURES_MIGRATIONS_FOLDER}
    # without file config.yaml (even empty), hasura migrate apply will fail
    touch ${FIXTURES_FOLDER}/${FIXTURES_SET}/config.yaml
done