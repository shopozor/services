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
        sh "make up"
      }
    }
    stage('Perform GraphQL engine tests') {
      steps {
        sh "make test.database-service"
      }
    }
    // stage('Perform backend integration tests') {
    //   steps {
    //     sh "make test.behave"
    //   }
    // }
    stage('Perform ui unit tests') {
      steps {
        sh "make test.ui-unit-tests"
      }
    }
    stage('Perform ui integration tests') {
      steps {
        sh "USER=`id -u` make test.ui-integration-tests"
      }
    }
    stage('Perform e2e tests') {
      steps {
        sh "USER=`id -u` make test.e2e-tests"
      }
    }
    // TODO: this needs rework!
    stage('Building specification') {
      environment {
        SOFTOZOR_CREDENTIALS = credentials('softozor-credentials')
      }
      steps {
        script {
          if(GIT_BRANCH == 'origin/dev' || GIT_BRANCH == 'origin/master') {
            build job: 'specification', parameters: [
              string(name: 'BRANCH', value: GIT_BRANCH.split('/')[1])
            ]
          }
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