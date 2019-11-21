#! /bin/bash

FIXTURES_FOLDER=fixtures
DATABASE_FIXTURES_FOLDER=${FIXTURES_FOLDER}/database
GRAPHQL_RESPONSES_FOLDER=${FIXTURES_FOLDER}/graphql-responses
APP_ROOT=.

GENERATE_JSON_FIXTURES=${APP_ROOT}/generate_json_fixtures.py
JSON_TO_SQL=${APP_ROOT}/json2sql.py


# Generate the json fixtures
python ${GENERATE_JSON_FIXTURES} -o ${DATABASE_FIXTURES_FOLDER}

# Generate the sql migrations based on the json fixtures
for FIXTURES_SET in tiny small medium large ; do
    FIXTURES_MIGRATIONS_FOLDER=${DATABASE_FIXTURES_FOLDER}/${FIXTURES_SET}/migrations
    if [ ! -d ${FIXTURES_MIGRATIONS_FOLDER} ]; then mkdir -p ${FIXTURES_MIGRATIONS_FOLDER}; fi
    for persona in consumers producers managers rex softozor; do
        python ${JSON_TO_SQL} -i ${DATABASE_FIXTURES_FOLDER}/${FIXTURES_SET}/Users/$persona.json -n shopozor-$persona -o ${FIXTURES_MIGRATIONS_FOLDER}
    done
    python ${JSON_TO_SQL} -i ${DATABASE_FIXTURES_FOLDER}/${FIXTURES_SET}/Shopozor.json -n shopozor-data -o ${FIXTURES_MIGRATIONS_FOLDER}
    # without file config.yaml (even empty), hasura migrate apply will fail
    touch ${DATABASE_FIXTURES_FOLDER}/${FIXTURES_SET}/config.yaml
done

# Generate graphql responses
python ./generate_graphql_responses.py -o ${GRAPHQL_RESPONSES_FOLDER} -i ${DATABASE_FIXTURES_FOLDER} --fixtures-set all