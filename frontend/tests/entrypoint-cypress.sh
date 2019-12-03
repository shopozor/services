#! /bin/bash

if [ $# -ne 1 ] ; then
  echo "Usage: $0 <cypress-test-type>"
  echo "Example: $0 integration"
  echo "Example: $0 e2e"
  exit 1
fi

TEST_TYPE=$1

for app in admin-ui consumer-ui ; do
  rm -Rf /app/frontend/$app/cypress/screenshots/* /app/frontend/$app/cypress/videos/*
  cd /app/frontend/$app
  CYPRESS_baseUrl="http://$app:4000/#" cypress run --env configFile=$TEST_TYPE
done