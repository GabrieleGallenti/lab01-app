pipeline {
  agent any
  options { timestamps() }
  parameters {
    booleanParam(name: 'BUILD_IMAGE', defaultValue: true, description: 'Costruisci anche l immagine Docker')
  }
  environment {
    IMAGE = "lab01:${BUILD_NUMBER}"
  }
  stages {
    stage('Test') {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt pytest ruff
          ruff check .
          pytest -q --junitxml=report.xml
        '''
      }
      post {
        always { junit 'report.xml' }
      }
    }
    stage('Build') {
      when { expression { params.BUILD_IMAGE } }
      steps {
        sh 'docker build -t $IMAGE .'
      }
    }
    stage('Credenziale di prova') {
      steps {
        withCredentials([string(credentialsId: 'lab-token', variable: 'TOKEN')]) {
          sh 'echo "Il token è lungo ${#TOKEN} caratteri"; echo "Valore: $TOKEN"'
        }
      }
    }
  }
  post {
    success { echo 'Pipeline completata' }
    failure { echo 'Pipeline fallita: guarda i report dei test' }
  }
}
