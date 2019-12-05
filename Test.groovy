pipeline {
  agent any
  environment {
    API_PORT = 8081
    TEST_REPORTS_FOLDER = 'test-reports'
  }
  stages {
    stage('Build the docker images') {
      steps {
        sh "make build"
      }
    }
    stage('Fetch node dependencies') {
      steps {
        sh "make bootstrap"
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
        sh "make up"
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
    failure {
      build job: 'specification', parameters: [
        string(name: 'BRANCH', value: GIT_BRANCH.split('/')[1])
      ]
      build job: 'publish-docker-images', parameters: [
        string(name: 'TAG', value: GIT_BRANCH.split('/')[1]),
        string(name: 'BUILD_TYPE', value: 'production')
      ]
      build job: 'publish-docker-images', parameters: [
        string(name: 'TAG', value: GIT_BRANCH.split('/')[1]),
        string(name: 'BUILD_TYPE', value: 'e2e')
      ]
    }
  }
}