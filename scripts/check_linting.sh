#! /bin/bash

pre-commit run --all-files
EXIT_CODE=$(git ls-files -m | wc -l)
exit ${EXIT_CODE}