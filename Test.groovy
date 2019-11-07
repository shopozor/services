def helpers = new ch.softozor.pipeline.Helpers()
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
        script {
          helpers.deleteFolder('fixtures')
          sh "chmod u+x ./fixtures-generator/entrypoint.sh"
          sh "docker-compose -f docker-compose-tests.yaml up fixtures-service"
        }
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
      script {
        sh "docker-compose down"
        helpers.deleteFolder('fixtures')
        junit "**/test-report.xml"
      }
    }
  }
}