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
    stage('Build and publish fixtures generator') {
      steps {
        script {
          if(BUILD_TYPE == 'production') {
            serviceName = 'fixtures-generator'
            dockerRepoName = "$DOCKER_CREDENTIALS_USR/$serviceName:${TAG}"
            sh "docker build -t $dockerRepoName --file ./$serviceName/Dockerfile ."
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
            sh "docker build -t $dockerRepoName --target app --file ./$serviceName/Dockerfile ."
            sh "docker push $dockerRepoName"
          }
        }
      }
    }
    stage('Build and publish ui service') {
      steps {
        script {
          serviceName = 'ui'
          dockerRepoName = "$DOCKER_CREDENTIALS_USR/$serviceName:${TAG}"
          if(BUILD_TYPE == 'production') {
            sh "docker build --build-arg GRAPHQL_API=${GRAPHQL_API_URL} -t $dockerRepoName --target app --file ./$serviceName/Dockerfile ."
          } else {
            dockerRepoName += '-e2e'
            split_url = GRAPHQL_API_URL.split('.')
            staging_url = split_url[0] + '-staging' + split_url[1:-1]
            sh "docker build --build-arg GRAPHQL_API=$staging_url -t $dockerRepoName --target e2e --file ./$serviceName/Dockerfile ."
          }
          sh "docker push $dockerRepoName"
        }
      }
    }
  }
}