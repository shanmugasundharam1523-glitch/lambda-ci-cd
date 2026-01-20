pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = "ap-south-1"
        FUNCTION_NAME = "jenkins-backend"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Package Lambda') {
            steps {
                sh '''
                zip -r function.zip lambda_function.py
                '''
            }
        }

        stage('Deploy Lambda') {
            steps {
                sh '''
                aws lambda update-function-code                   --function-name $FUNCTION_NAME                   --zip-file fileb://function.zip
                '''
            }
        }
    }
}
