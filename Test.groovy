pipeline {
  agent any
  environment {
    REPORTS_FOLDER = 'junit-reports'
  }
  stages {
    stage('GraphQL engine tests') {
      steps {
        sh "docker-compose -f /var/jenkins_home/workspace/docker-compose-test/docker-compose-tests.yaml up --abort-on-container-exit"
      }
    }
  }
  post {
    always {
      script {
         junit "**/test-report.xml"
      }
    }
  }
}