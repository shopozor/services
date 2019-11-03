pipeline {
  agent any
  stages {
    // stage('Start GraphQL engine') {
    //   steps {
    //     sh "docker-compose -f docker-compose-tests.yaml up graphql-engine"
    //     // TODO: wait until service is up: curl http://localhost:9000/v1/version until it returns the version {"version":"v1.0.0-beta.9"}
    //   }
    // }
    stage('Test GraphQL engine') {
      steps {
        sh "docker-compose -f docker-compose-tests.yaml up --abort-on-container-exit hasura-service-tests"
      }
    }
  }
  post {
    always {
      sh "docker-compose down"
    }
    always {
      junit "**/test-report.xml"
    }
  }
}