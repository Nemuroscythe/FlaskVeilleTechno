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
        stage('Code quality') {
            steps {
                bat 'call venv/Scripts/activate.bat && pylint main --output-format=parseable > pylint-report.txt || exit 0'
            }
        }
        stage('Approval'){
            when {
                branch 'release/*'
            }
            steps {
                input message: 'Est ce que vous approuvez le déploiement (vérifier les rapports)?', ok: 'Approuver'
            }
        }
        stage('Deploy to DEV') {
            when {
                branch 'feature/*'
            }
            steps {
                bat "pscp -pw ${env.DEPLOY_PASSWORD} -r ${env.WORKSPACE} ${env.DEPLOY_USERNAME}@${env.DEV_BASE_URL}:${env.DEPLOY_PATH}"
            }
        }
        stage('Deploy to ACC') {
            when {
                branch 'master'
            }
            steps {
                script {
                    def remoteHost = ${env.DEV_BASE_URL}
                    def remoteUser = ${env.DEPLOY_USERNAME}
                    def remotePassword = ${env.DEPLOY_PASSWORD}
                    def localDir = ${env.WORKSPACE}
                    def remoteDir = ${env.DEPLOY_PATH}
                    bat 'winscp.com /log=winscp.log /command "open sftp://' + remoteUser + ':' + remotePassword + '@' + remoteHost + '" "put ' + localDir + '/* ' + remoteDir + '/" "exit"'
                }
            }
        }
        stage('Deploy to PRD') {
            when {
                branch 'release/*'
            }
            steps {
                bat "pscp -pw ${env.DEPLOY_PASSWORD} -r ${env.BUILD_FILES} ${env.DEPLOY_USERNAME}@${env.DEV_BASE_URL}:${env.DEPLOY_PATH}"
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