pipeline {
  agent any
  stages {
    stage('Build the docker images') {
      steps {
        sh "docker-compose build"
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
        sh "docker-compose -f docker-compose-tests.yaml up hasura-service-tests"
      }
    }
  }
  post {
    always {
      sh "docker-compose down"
      junit "**/test-report.xml"
    }
  }
}