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
        stage('Deliver') {
            steps {
                script {
                    // Define the remote server's IP address, username, and password
                    def remoteIp = 'ssh-snacknbite.alwaysdata.net'
                    def remoteUser = 'snacknbite'
                    def remotePassword = 'SnackNBiteIETCPS100!'

                    // Define the local and remote file paths
                    def localPath = 'E:/JenkinsAgent/workspace/CICDPipeline/*'
                    def remotePath = 'atc'
                    // Execute the pscp command to copy the files to the remote server
                    bat "pscp -pw ${remotePassword} -r ${localPath} ${remoteUser}@${remoteIp}:${remotePath}"
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