pipeline {
  agent any
  environment {
    REPORTS_FOLDER = 'junit-reports'
  }
  stages {
    // sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    // sudo chmod +x /usr/local/bin/docker-compose
    stage('GraphQL engine tests') {
      steps {
        sh "docker-compose -f /var/jenkins_home/workspace/docker-compose-test/docker-compose-tests.yaml up --abort-on-container-exit"
      }
    }
  }
  post {
    always {
      script {
         junit "**/$REPORTS_FOLDER/*.xml"
      }
    }
  }
}