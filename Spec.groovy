pipeline {
  agent any
  environment {
    SOFTOZOR_CREDENTIALS = credentials('softozor-credentials')
  }
  stages {
    stage('Admin UI specification generation') {
      steps {
        script {
          uiName = 'admin-ui'
          featureDir = "$WORKSPACE/frontend/${uiName}/cypress/e2e"
          sh "mono /opt/pickles/Pickles.exe --feature-directory=$featureDir --output-directory=specification --system-under-test-name=${uiName} --system-under-test-version=$GIT_COMMIT --language=fr --documentation-format=dhtml --exp --et 'in-preparation'"
          sh "sshpass -p $SOFTOZOR_CREDENTIALS_PSW ssh -o StrictHostKeyChecking=no $SOFTOZOR_CREDENTIALS_USR@softozor.ch 'rm -Rf ~/www/www.softozor.ch/shopozor/${uiName}'"
          sh "sshpass -p $SOFTOZOR_CREDENTIALS_PSW scp -o StrictHostKeyChecking=no -r specification/* $SOFTOZOR_CREDENTIALS_USR@softozor.ch:~/www/www.softozor.ch/shopozor/${uiName}"
        }
      }
    }
    stage('Consumer UI specification generation') {
      steps {
        script {
          uiName = 'consumer-ui'
          featureDir = "$WORKSPACE/frontend/${uiName}/cypress/e2e"
          sh "mono /opt/pickles/Pickles.exe --feature-directory=$featureDir --output-directory=specification --system-under-test-name=${uiName} --system-under-test-version=$GIT_COMMIT --language=fr --documentation-format=dhtml --exp --et 'in-preparation'"
          sh "sshpass -p $SOFTOZOR_CREDENTIALS_PSW ssh -o StrictHostKeyChecking=no $SOFTOZOR_CREDENTIALS_USR@softozor.ch 'rm -Rf ~/www/www.softozor.ch/shopozor/${uiName}'"
          sh "sshpass -p $SOFTOZOR_CREDENTIALS_PSW scp -o StrictHostKeyChecking=no -r specification/* $SOFTOZOR_CREDENTIALS_USR@softozor.ch:~/www/www.softozor.ch/shopozor/${uiName}"
        }
      }
    }
  }
}