#! /bin/bash

pytest --hasura-endpoint http://graphql-engine:8080 -ra --junitxml=test-reports/test-report.xml -vv