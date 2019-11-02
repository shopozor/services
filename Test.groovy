pipeline {
  agent any
  stages {
    stage('GraphQL engine tests') {
      steps {
        sh "docker-compose -f docker-compose-tests.yaml up --abort-on-container-exit hasura-service-tests"
      }
    }
  }
  post {
    always {
      script {
        junit "**/test-report.xml"
      }
    }
    // TODO: this needs to be done ALL the time, not only upon failure!
    failure {
      sh "docker-compose down"
    }
  }
}