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
        sh "docker-compose down"
        junit "**/test-report.xml"
      }
    }
  }
}