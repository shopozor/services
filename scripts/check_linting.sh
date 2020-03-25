#! /bin/bash

pre-commit run --all-files
EXIT_CODE=$(git ls-files -m | wc -l)
if [ "${EXIT_CODE}" -ne "0" ] ; then
  echo "List of changed files: "
  git ls-files -m
fi
exit ${EXIT_CODE}