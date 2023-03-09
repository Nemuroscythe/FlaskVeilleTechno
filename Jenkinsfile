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
                bat 'call venv/Scripts/activate.bat && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'call venv/Scripts/activate.bat && pytest --cov=main --cov-report=xml:coverage.xml'
                bat 'python -m pytest'
            }
        }
        stage('Test code quality') {
            steps {
                bat 'call venv/Scripts/activate.bat && pylint main --output-format=parseable > pylint-report.txt || exit 0'
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
            }
        }
    }
     post {
        always {
            cobertura coberturaReportFile: '**/coverage.xml'
            recordIssues tool: pyLint(pattern: '**/pylint-report.txt'), enabledForFailure: true
        }
    }
}
