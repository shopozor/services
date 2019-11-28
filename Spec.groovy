pipeline {
  agent any
  stages {
    stage('Spec generation') {
      environment {
        SOFTOZOR_CREDENTIALS = credentials('softozor-credentials')
      }
      steps {
        script {
          featureDir = "$WORKSPACE/ui/cypress/e2e"
          sh "mono /opt/pickles/Pickles.exe --feature-directory=$featureDir --output-directory=specification --system-under-test-name=shopozor --system-under-test-version=$GIT_COMMIT --language=fr --documentation-format=dhtml --exp --et 'in-preparation'"
          sh "sshpass -p $SOFTOZOR_CREDENTIALS_PSW ssh -o StrictHostKeyChecking=no $SOFTOZOR_CREDENTIALS_USR@softozor.ch 'rm -Rf ~/www/www.softozor.ch/shopozor/*'"
          sh "sshpass -p $SOFTOZOR_CREDENTIALS_PSW scp -o StrictHostKeyChecking=no -r specification/* $SOFTOZOR_CREDENTIALS_USR@softozor.ch:~/www/www.softozor.ch/shopozor/"
        }
      }
    }
  }
}