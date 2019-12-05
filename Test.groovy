pipeline {
  agent any
  environment {
    API_PORT = 8081
    TEST_REPORTS_FOLDER = 'test-reports'
  }
  stages {
    stage('Lint code') {
      environment {
        GITHUB_CREDENTIALS = credentials('github-credentials')
      }
      steps {
        script {
          sh "pre-commit run --all-files"
          sh "git add ."
          originUrl = "https://$GITHUB_CREDENTIALS_USR:$GITHUB_CREDENTIALS_PSW@" + GIT_URL.drop(8)
          sh "git remote rm origin"
          sh "git remote add origin $originUrl"
          sh "git commit -m 'automatic linting'"
          sh "git push"
        }
      }
    }
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
  }
}