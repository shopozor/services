#! /bin/bash

TEST_REPORTS_FOLDER=${1:-test-reports}

behave --junit --junit-directory ${TEST_REPORTS_FOLDER} --tags ~wip