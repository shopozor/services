#! /bin/bash

FIXTURES_FOLDER=fixtures
DATABASE_FIXTURES_FOLDER=${FIXTURES_FOLDER}/database
GRAPHQL_RESPONSES_FOLDER=${FIXTURES_FOLDER}/graphql/responses
APP_ROOT=.
FIXTURES_SET=${1:-medium}

GENERATE_JSON_FIXTURES=${APP_ROOT}/generate_json_fixtures.py
JSON_TO_SQL=${APP_ROOT}/json2sql.py

# Clean up existing fixtures
[[ -d ${FIXTURES_FOLDER} ]] && rm -Rf ${FIXTURES_FOLDER}/* || mkdir ${FIXTURES_FOLDER}
[[ -d ${GRAPHQL_RESPONSES_FOLDER} ]] && rm -Rf ${GRAPHQL_RESPONSES_FOLDER}/*

# Generate the json fixtures
python ${GENERATE_JSON_FIXTURES} -o ${DATABASE_FIXTURES_FOLDER} --fixtures-set ${FIXTURES_SET}

# Generate the sql migrations based on the json fixtures
FIXTURES_MIGRATIONS_FOLDER=${DATABASE_FIXTURES_FOLDER}/migrations
if [ ! -d ${FIXTURES_MIGRATIONS_FOLDER} ]; then mkdir -p ${FIXTURES_MIGRATIONS_FOLDER}; fi
python ${JSON_TO_SQL} -i ${DATABASE_FIXTURES_FOLDER}/Images.json -n shopozor-images -o ${FIXTURES_MIGRATIONS_FOLDER}
# The order is important because we reset the auto-incrementation of the users' ids in each sql
for persona in softozor rex managers producers consumers; do
    python ${JSON_TO_SQL} -i ${DATABASE_FIXTURES_FOLDER}/Users/$persona.json -n shopozor-$persona -o ${FIXTURES_MIGRATIONS_FOLDER}
done
python ${JSON_TO_SQL} -i ${DATABASE_FIXTURES_FOLDER}/Shopozor.json -n shopozor-data -o ${FIXTURES_MIGRATIONS_FOLDER}
# without file config.yaml (even empty), hasura migrate apply will fail
touch ${DATABASE_FIXTURES_FOLDER}/config.yaml

# Generate graphql responses
python ./generate_graphql_responses.py -o ${GRAPHQL_RESPONSES_FOLDER} -i ${DATABASE_FIXTURES_FOLDER}