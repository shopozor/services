pipeline {
  agent any
  stages {
    stage('GraphQL engine tests') {
      steps {
        sh "docker-compose -f docker-compose-tests.yaml up postgres graphql-engine hasura-service-tests --abort-on-container-exit"
      }
    }
  }
  post {
    always {
      script {
         junit "**/test-report.xml"
      }
    }
    failure {
      sh "docker-compose down"
    }
  }
}