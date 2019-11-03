#! /bin/bash

FIXTURES_SET=${1:-small}
FIXTURES_FOLDER=${2:-database-service/fixtures}
FIXTURES_MIGRATIONS_FOLDER=${3:-${FIXTURES_FOLDER}/migrations}

GENERATE_JSON_FIXTURES=database-service/tests/fixtures-generator/generate_json_fixtures.py
JSON_TO_SQL=database-service/tests/fixtures-generator/json2sql.py

python ${GENERATE_JSON_FIXTURES} -o ${FIXTURES_FOLDER}
python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Users/Consommateurs.json -n shopozor-consumers -o ${FIXTURES_MIGRATIONS_FOLDER}
python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Users/Producteurs.json -n shopozor-producers -o ${FIXTURES_MIGRATIONS_FOLDER}
python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Users/Responsables.json -n shopozor-managers -o ${FIXTURES_MIGRATIONS_FOLDER}
python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Users/Rex.json -n shopozor-rex -o ${FIXTURES_MIGRATIONS_FOLDER}
python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Users/Softozor.json -n shopozor-softozor -o ${FIXTURES_MIGRATIONS_FOLDER}
python ${JSON_TO_SQL} -i ${FIXTURES_FOLDER}/${FIXTURES_SET}/Shopozor.json -n shopozor-data -o ${FIXTURES_MIGRATIONS_FOLDER}