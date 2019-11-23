pipeline {
  agent any
  environment {
    API_PORT = 8081
    TEST_REPORTS_FOLDER = 'test-reports'
  }
  stages {
    stage('Build the docker images') {
      steps {
        sh "docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml build"
      }
    }
    stage('Generate the database fixtures') {
      steps {
        script {
          sh "rm -Rf fixtures && mkdir fixtures"
          sh "chmod u+x ./fixtures-generator/entrypoint.sh"
          // without that USER variable, it is not possible to delete the generated fixtures folder anymore
          sh "USER=`id -u` docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up fixtures-service"
        }
      }
    }
    stage('Start GraphQL engine') {
      steps {
        sh "docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up -d postgres graphql-engine"
        sh "chmod u+x ./database-service/scripts/waitForService.sh && ./database-service/scripts/waitForService.sh localhost ${API_PORT}"
      }
    }
    stage('Perform GraphQL engine tests') {
      steps {
        sh "docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up hasura-service-tests"
      }
    }
    stage('Perform acceptance tests') {
      steps {
        sh "docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up features-tests"
      }
    }
  }
  post {
    always {
      sh "docker-compose down"
      junit "**/${TEST_REPORTS_FOLDER}/*.xml"
    }
  }
}