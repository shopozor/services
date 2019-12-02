pipeline {
  agent any
  environment {
    API_PORT = 8081
    TEST_REPORTS_FOLDER = 'test-reports'
  }
  stages {
    stage('Build the docker images') {
      steps {
        sh "make build"
      }
    }
    stage('Fetch node dependencies') {
      steps {
        sh "yarn && yarn bootstrap"
      }
    }
    stage('Generate the database fixtures') {
      steps {
        script {
          sh "make fixtures.clean"
          sh "mkdir fixtures"
          // without that USER_ID variable, it is not possible to delete the generated fixtures folder anymore
          sh "chmod u+x ./backend/fixtures-generator/entrypoint.sh"
          sh "USER_ID=`id -u` docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up fixtures-service"
        }
      }
    }
    stage('Start services') {
      steps {
        sh "make up"
      }
    }
    stage('Perform GraphQL engine tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
          sh "chmod u+x ./backend/database-service/tests/entrypoint.sh"
          sh "USER_ID=`id -u` docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up --abort-on-container-exit hasura-service-tests"
        }
      }
    }
    stage('Perform ui unit tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
         sh "chmod u+x ./frontend/tests/entrypoint-unit.sh"
         sh "USER_ID=`id -u` docker-compose -f docker-compose.yaml -f docker-compose-ui.yaml -f docker-compose-ui-tests.yaml up --abort-on-container-exit ui-unit-tests"
        }
      }
    }
    stage('Perform ui integration tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
          sh "chmod u+x ./frontend/entrypoint-integration.sh"
	        sh "USER_ID=`id -u` docker-compose -f docker-compose.yaml -f docker-compose-ui.yaml -f docker-compose-ui-tests.yaml up --abort-on-container-exit ui-integration-tests"
        }
      }
    }
    stage('Perform e2e tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
          sh "chmod u+x ./frontend/entrypoint-e2e.sh"
        	sh "USER_ID=`id -u` docker-compose -f docker-compose.yaml -f docker-compose-ui.yaml -f docker-compose-ui-tests.yaml up --abort-on-container-exit e2e-tests"
        }
      }
    }
  }
  post {
    always {
      sh "make down"
      junit "**/test-reports/*.xml"
    }
  }
}