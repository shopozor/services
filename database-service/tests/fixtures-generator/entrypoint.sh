#! /bin/bash

FIXTURES_SET=${1:-small}
FIXTURES_FOLDER=${2:-database-service/fixtures}
FIXTURES_MIGRATIONS_FOLDER=${3:-${FIXTURES_FOLDER}/migrations}

GENERATE_JSON_FIXTURES=database-service/tests/fixtures-generator/generate_json_fixtures.py
JSON_TO_SQL=database-service/tests/fixtures-generator/json2sql.py

python ${GENERATE_JSON_FIXTURES} -o ${FIXTURES_FOLDER}
for persona in consumers producers managers rex softozor; do
    python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Users/$persona.json -n shopozor-$persona -o ${FIXTURES_MIGRATIONS_FOLDER}
done
python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Shopozor.json -n shopozor-data -o ${FIXTURES_MIGRATIONS_FOLDER}