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
        // all the involved services need to be mentioned here otherwise they will not be aborted
        sh "docker-compose -f docker-compose-tests.yaml up --abort-on-container-exit postgres graphql-engine hasura-service-tests"
      }
    }
  }
  post {
    failure {
      // upon failure in the docker-compose command, the containers might not be shut down
      // therefore we enforce it here
      sh "docker-compose down"
    }
    always {
      junit "**/test-report.xml"
    }
  }
}