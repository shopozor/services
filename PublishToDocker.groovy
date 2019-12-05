pipeline {
  agent any
  environment {
    DOCKER_CREDENTIALS = credentials('docker-credentials')
    PRODUCT = ${DOCKER_CREDENTIALS_USR}
  }
  stages {
    stage('Log into docker registry') {
      steps {
        sh "docker login -u $DOCKER_CREDENTIALS_USR -p $DOCKER_CREDENTIALS_PSW"
      }
    }
    stage('Build and publish fixtures generator') {
      steps {
        script {
          serviceName = 'fixtures-service'
          if(BUILD_TYPE == 'production') {
            sh "docker-compose -f docker-compose-backend.yaml ${serviceName}"
            sh "docker push ${PRODUCT}/${serviceName}:${TAG}"
          }
        }
      }
    }
    stage('Build and publish database service') {
      steps {
        script {
          serviceName = 'database-service'
          if(BUILD_TYPE == 'production') {
            sh "docker-compose -f docker-compose-backend.yaml ${serviceName}"
            sh "docker push ${PRODUCT}/${serviceName}:${TAG}"
          }
        }
      }
    }
    // we don't publish any ui docker image as they will never be used (we deploy static content or SPAs)
  }
}