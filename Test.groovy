pipeline {
  agent any
  stages {
    stage('Start GraphQL engine') {
      steps {
        sh "docker-compose -f docker-compose-tests.yaml up graphql-engine"
        sh "chmod u+x ./database-service/scripts/waitForService.sh && ./database-service/scripts/waitForService.sh localhost 9000"
      }
    }
    stage('Test GraphQL engine') {
      steps {
        // all the involved services need to be mentioned here otherwise they will not be aborted
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