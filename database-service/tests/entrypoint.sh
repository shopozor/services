#! /bin/bash

pytest --hasura-endpoint http://graphql-engine:8080 --root /app -ra --junitxml=test-reports/test-report.xml