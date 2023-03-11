pipeline {
    agent {
        node {
            label 'test_agent'
            }
    }
    triggers {
        pollSCM('*/5 * * * *')
        cron('0 16 * * *')
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
        stage('Approval'){
            steps {
                input message: 'Do you want to deploy?', ok: 'Yes', parameters: [
                    string(defaultValue: 'Yes', description: 'Yes or No', name: 'Deploy?')
                ]
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Execute the pscp command to copy the files to the remote server
                    bat "pscp -pw ${env.DEPLOY_PASSWORD} -r ${env.BUILD_FILES} ${env.DEPLOY_USERNAME}@${env.DEV_BASE_URL}:${env.DEPLOY_PATH}"
                }
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