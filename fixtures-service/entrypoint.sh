#! /bin/bash

FIXTURES_SET=${1:-small}

 python fixtures-service/generate_json_fixtures.py -o fixtures
 python fixtures-service/json2sql.py -i fixtures/${FIXTURES_SET}/Users/Consommateurs.json -n shopozor-consumers -o database-service/migrations
 python fixtures-service/json2sql.py -i fixtures/${FIXTURES_SET}/Users/Producteurs.json -n shopozor-producers -o database-service/migrations
 python fixtures-service/json2sql.py -i fixtures/${FIXTURES_SET}/Users/Responsables.json -n shopozor-managers -o database-service/migrations
 python fixtures-service/json2sql.py -i fixtures/${FIXTURES_SET}/Users/Rex.json -n shopozor-rex -o database-service/migrations
 python fixtures-service/json2sql.py -i fixtures/${FIXTURES_SET}/Users/Softozor.json -n shopozor-softozor -o database-service/migrations
 python fixtures-service/json2sql.py -i fixtures/${FIXTURES_SET}/Shopozor.json -n shopozor-data -o database-service/migrations