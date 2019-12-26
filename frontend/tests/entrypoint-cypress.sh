#! /bin/bash

if [ $# -ne 1 ] ; then
  echo "Usage: $0 <cypress-test-type>"
  echo "Example: $0 integration"
  echo "Example: $0 e2e"
  exit 1
fi

TEST_TYPE=$1

yarn cypress:clean
for app in admin consumer ; do
  lerna run cypress:${TEST_TYPE}:ci --scope $app-ui --stream
done