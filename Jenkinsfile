pipeline {
  agent any

  environment {
    AWS_REGION = "ap-south-1"
    EKS_CLUSTER = "my-eks-cluster"
  }

  stages {

    stage("Deploy to EKS") {
      steps {
        sh '''
          echo "🔍 Workspace"
          pwd

          echo "📂 List k8s directory"
          ls -l k8s/

          echo "📄 Apply backend deployment"
          kubectl apply -f k8s/backend-deployment.yaml

          echo "📄 Apply backend service"
          kubectl apply -f k8s/backend-service.yaml

          echo "📦 Deployments"
          kubectl get deployments

          echo "🚀 Rollout status"
          kubectl rollout status deployment/backend
        '''
      }
    }

  }
}
