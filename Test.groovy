pipeline {
  agent any
  environment {
    API_PORT = 8081
    USER=1000
  }
  stages {
    stage('Build the docker images') {
      steps {
        sh "make build"
      }
    }
    stage('Generate the database fixtures') {
      steps {
        script {
          sh "make fixtures.clean"
          sh "mkdir fixtures && mkdir graphql/responses"
          // without that USER variable, it is not possible to delete the generated fixtures folder anymore
          // sh "make fixtures.generate"
          sh "chmod u+x ./fixtures-generator/entrypoint.sh"
          sh "docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up fixtures-service"
        }
      }
    }
    stage('Start services') {
      steps {
        // sh "make up"
        sh "docker-compose -f docker-compose-tests.yaml up -d postgres graphql-engine"
        sh "chmod u+x ./database-service/scripts/waitForService.sh && ./database-service/scripts/waitForService.sh localhost ${API_PORT}"
      }
    }
    stage('Perform GraphQL engine tests') {
      steps {
        sh "make test.database-service"
      }
    }
    stage('Perform ui unit tests') {
      steps {
        sh "make test.ui-unit-tests"
      }
    }
    stage('Perform ui integration tests') {
      steps {
        sh "make test.ui-integration-tests"
      }
    }
    stage('Perform e2e tests') {
      steps {
        sh "make test.e2e-tests"
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