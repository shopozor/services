pipeline {
  agent any
  stages {
    stage('Build the docker images') {
      steps {
        sh "docker-compose -f docker-compose-tests.yaml build"
      }
    }
    stage('Generate the database fixtures') {
      steps {
        sh "docker-compose -f docker-compose-tests.yaml up fixtures-service"
      }
    }
    stage('Start GraphQL engine') {
      steps {
        sh "docker-compose -f docker-compose-tests.yaml up -d postgres graphql-engine"
        sh "chmod u+x ./database-service/scripts/waitForService.sh && ./database-service/scripts/waitForService.sh localhost 9000"
      }
    }
    stage('Test GraphQL engine') {
      steps {
        sh "chmod u+x ./database-service/tests/fixtures-generator/entrypoint.sh"
        sh "docker-compose -f docker-compose-tests.yaml up hasura-service-tests"
      }
    }
  }
  post {
    always {
      sh "docker-compose down"
      sh "rm -Rf fixtures"
      junit "**/test-report.xml"
    }
  }
}