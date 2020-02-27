#! /bin/bash

ENDPOINT=${1:-http://api:8080/}

pytest -ra --junitxml=test-reports/test-report.xml -vv --hasura-endpoint $ENDPOINT