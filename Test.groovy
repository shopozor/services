pipeline {
  agent any
  environment {
    API_PORT = 8081
    ASSETS_API = "http://localhost:9001"
    GENERATOR_API_PORT = 2000
    GENERATOR_API = "http://localhost:${GENERATOR_API_PORT}/"
    GRAPHQL_API = "http://localhost:${API_PORT}/v1/graphql/"
    TEST_REPORTS_FOLDER = 'test-reports'
  }
  stages {
    // The code linting stage needs node modules like the linter
    stage('Bootstrap node packages') {
      steps {
        sh "make bootstrap"
      }
    }
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
        sh "yarn build"
        sh "make --directory backend static-site.generate"
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
          sh "make --directory backend assets.up"
          sh "make --directory backend seed-database"
          sh "make --directory backend test.integration"
          sh "make --directory backend unseed-database"
          sh "make --directory backend assets.down"
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
          sh "make --directory backend assets.up"
          sh "make --directory backend seed-database"
        	sh "make --directory frontend test.e2e"
          sh "make --directory backend unseed-database"
          sh "make --directory backend assets.down"
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