pipeline {
    agent {
        node {
            label 'test_agent'
            }
      }
    stages {
        stage('Build') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate.bat'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
            }
        }
    }
}
