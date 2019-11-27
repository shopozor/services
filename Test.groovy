pipeline {
  agent any
  environment {
    API_PORT = 8081
  }
  stages {
    stage('Build the docker images') {
      steps {
        sh "env"
        sh "make build"
      }
    }
    stage('Generate the database fixtures') {
      steps {
        script {
          sh "make fixtures.clean"
          sh "mkdir fixtures && mkdir -p graphql/responses"
          // without that USER variable, it is not possible to delete the generated fixtures folder anymore
          // sh "make USER=`id -u` fixtures.generate"
          sh "chmod u+x ./fixtures-generator/entrypoint.sh"
          sh "USER=`id -u` docker-compose -f docker-compose.yaml -f docker-compose-tests.yaml up fixtures-service"
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
          sh "make test.database-service"
        }
      }
    }
    stage('Perform ui unit tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
         sh "make test.ui-unit"
        }
      }
    }
    stage('Perform ui integration tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
          sh "make test.ui-integration"
        }
      }
    }
    stage('Perform e2e tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
          sh "make test.e2e"
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