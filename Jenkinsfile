pipeline {
  agent any

  environment {
    AWS_DEFAULT_REGION = "ap-south-1"
    AWS_ACCOUNT_ID     = "204107104458"
    ECR_REPO_NAME      = "ecs-backend-app"
    ECR_REPO_URI       = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${ECR_REPO_NAME}"
    ECS_CLUSTER        = "ecs-backend-cluster"
    ECS_SERVICE        = "ecs-backend-task-service-3euf1w4y"
    TASK_FAMILY        = "ecs-backend-task"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        sh '''
        docker build -t ${ECR_REPO_NAME}:latest .
        '''
      }
    }

    stage('Login to ECR') {
      steps {
        sh '''
        aws ecr get-login-password --region ${AWS_DEFAULT_REGION} \
        | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com
        '''
      }
    }

    stage('Tag & Push Image to ECR') {
      steps {
        sh '''
        docker tag ${ECR_REPO_NAME}:latest ${ECR_REPO_URI}:latest
        docker push ${ECR_REPO_URI}:latest
        '''
      }
    }

    stage('Register New Task Definition') {
      steps {
        sh '''
        sed "s|IMAGE_URI|${ECR_REPO_URI}:latest|g" task-definition.json > task-def-updated.json

        aws ecs register-task-definition \
          --cli-input-json file://task-def-updated.json
        '''
      }
    }

    stage('Update ECS Service') {
      steps {
        sh '''
        aws ecs update-service \
          --cluster ${ECS_CLUSTER} \
          --service ${ECS_SERVICE} \
          --task-definition ${TASK_FAMILY} \
          --force-new-deployment
        '''
      }
    }
  }
}
