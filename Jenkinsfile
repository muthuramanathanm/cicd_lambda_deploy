pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('8afb84c4-84e3-4720-8900-c53a5083424c')
        AWS_SECRET_ACCESS_KEY = credentials('8afb84c4-84e3-4720-8900-c53a5083424c')
        AWS_DEFAULT_REGION = 'us-east-1'
        LAMBDA_FUNCTION_NAME = 'lambda_function'
        GIT_REPO_URL = 'https://github.com/muthuramanathanm/cicd_lambda_deploy.git'
        PYTHON_FILE_PATH = 'lambda_function.py'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: 'github', url: GIT_REPO_URL
            }
        }

        stage('Deploy') {
            steps {
                script {
                    withAWS(region: AWS_DEFAULT_REGION, credentials: 'aws-credentials') {
                        sh "aws lambda update-function-code --function-name ${LAMBDA_FUNCTION_NAME} --zip-file fileb://${WORKSPACE}/${PYTHON_FILE_PATH}"
                    }
                }
            }
        }
    }
}
