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
                bat '''venv/Scripts/activate.bat
                pip install -r requirements.txt'''
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pytest'
            }
        }
        stage('Test code quality') {
            steps {
                echo "Testing code quality.."
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
            }
        }
    }
}
