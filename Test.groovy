pipeline {
  agent any
  environment {
    REPORTS_FOLDER = 'junit-reports'
  }
  stages {
    stage('GraphQL engine tests') {
      steps {
        // step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose-tests.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: true])
        // step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose-tests.yml', option: [$class: 'ExecuteCommandInsideContainer', command: 'pytest --hasura-endpoint http://graphql-engine:8080 -ra --junitxml=test-report.xml', index: 1, privilegedMode: false, service: 'hasura-service-tests', workDir: ''], useCustomDockerComposeFile: true])
        // step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose-tests.yml', option: [$class: 'StopAllServices'], useCustomDockerComposeFile: true])
        sh "docker-compose -f /var/jenkins_home/workspace/docker-compose-test/docker-compose-tests.yml up --abort-on-container-exit"
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