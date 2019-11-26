pipeline {
  agent any
  environment {
    API_PORT = 8081
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
          // without that USER variable, it is not possible to delete the generated fixtures folder anymore
          sh "USER=`id -u` make fixtures.generate"
        }
      }
    }
    stage('Start services') {
      steps {
        sh "API_PORT=${API_PORT} make up"
      }
    }
    stage('Perform GraphQL engine tests') {
      steps {
        sh "API_PORT=${API_PORT} make test.database-service"
      }
    }
    stage('Perform ui unit tests') {
      steps {
        sh "API_PORT=${API_PORT} make test.ui-unit-tests"
      }
    }
    stage('Perform ui integration tests') {
      steps {
        sh "API_PORT=${API_PORT} USER=`id -u` make test.ui-integration-tests"
      }
    }
    stage('Perform e2e tests') {
      steps {
        sh "API_PORT=${API_PORT} USER=`id -u` make test.e2e-tests"
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