pipeline {
  agent any
  environment {
    REPORTS_FOLDER = 'junit-reports'
  }
  stages {
    stage('GraphQL engine tests') {
    //   steps {
    //     sh ". $VENV/bin/activate && pytest -ra --junitxml=$REPORTS_FOLDER/shopozor-unit-tests.xml"
    //   }
      steps {
        step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose-tests.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: true])
      }
    }
  }
  post {
    always {
      script {
         junit "**/$REPORTS_FOLDER/*.xml"
      }
    }
  }
}