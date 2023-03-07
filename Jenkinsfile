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
                bat 'venv/Scripts/activate.bat'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'venv/Scripts/activate.bat & pytest --cov=main --cov-report=xml:coverage.xml'
                bat 'python -m pytest'
            }
        }
        stage('Test code quality') {
            steps {
                echo "pylint main"
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
            }
        }
    }
}
