pipeline {
  agent any
  environment {
    DOCKER_CREDENTIALS = credentials('docker-credentials')
  }
  stages {
    stage('Log into docker registry') {
      steps {
        sh "docker login -u $DOCKER_CREDENTIALS_USR -p $DOCKER_CREDENTIALS_PSW"
      }
    }
    // TODO: see if we can't take the images build in the docker-compose build step in the tests pipeline!
    stage('Build and publish fixtures generator') {
      steps {
        script {
          if(BUILD_TYPE == 'production') {
            serviceName = 'fixtures-generator'
            dockerRepoName = "$DOCKER_CREDENTIALS_USR/$serviceName:${TAG}"
            sh "docker build -t $dockerRepoName --file ./backend/$serviceName/Dockerfile ."
            sh "docker push $dockerRepoName"
          }
        }
      }
    }
    stage('Build and publish database service') {
      steps {
        script {
          if(BUILD_TYPE == 'production') {
            serviceName = 'database-service'
            dockerRepoName = "$DOCKER_CREDENTIALS_USR/$serviceName:${TAG}"
            sh "docker build -t $dockerRepoName --target app --file ./backend/$serviceName/Dockerfile ."
            sh "docker push $dockerRepoName"
          }
        }
      }
    }
    // we don't publish any ui docker image as they will never be used (we deploy static content or SPAs)
  }
}