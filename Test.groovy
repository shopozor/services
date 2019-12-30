pipeline {
  agent any
  environment {
    API_PORT = 8081
    GRAPHQL_API = "http://localhost:${API_PORT}/v1/graphql/"
    TEST_REPORTS_FOLDER = 'test-reports'
  }
  stages {
    stage('Lint code') {
      steps {
        script {
          sh "make lint"
        }
      }
    }
    stage('Build the services') {
      steps {
        sh "make build"
      }
    }
    stage('Generate the database fixtures') {
      steps {
        script {
          sh "make --directory backend fixtures.generate"
        }
      }
    }
    stage('Start services') {
      steps {
        sh "make --directory backend up"
      }
    }
    stage('Build the frontends') {
      steps {
        sh "make bootstrap"
        sh "yarn build"
      }
    }
    stage('Perform database tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
          sh "make --directory backend test.database-service"
        }
      }
    }
    stage('Perform backend services integration tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
          sh "make --directory backend seed-database"
          sh "make --directory backend test.integration"
          sh "make --directory backend unseed-database"
        }
      }
    }
    stage('Perform ui unit tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
         sh "make --directory frontend test.unit"
        }
      }
    }
    stage('Perform ui integration tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
	        sh "make --directory frontend test.integration"
        }
      }
    }
    stage('Perform e2e tests') {
      steps {
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
          sh "make --directory backend seed-database"
          // TODO: add a command to generate the static sites
        	sh "make --directory frontend test.e2e"
          sh "make --directory backend unseed-database"
        }
      }
    }
  }
  post {
    always {
      sh "make down"
      junit "**/test-reports/*.xml"
    }
    // This doesn't work; maybe we should perform these actions after merging the code
    /*success {
      build job: 'specification', parameters: [
        string(name: 'BRANCH', value: GIT_COMMIT)
      ]
      build job: 'publish-docker-images', parameters: [
        string(name: 'TAG', value: GIT_COMMIT),
        string(name: 'BUILD_TYPE', value: 'production')
      ]
      build job: 'publish-docker-images', parameters: [
        string(name: 'TAG', value: GIT_COMMIT),
        string(name: 'BUILD_TYPE', value: 'e2e')
      ]
    }*/
  }
}