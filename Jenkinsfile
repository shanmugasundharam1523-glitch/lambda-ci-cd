stage("Deploy to EKS") {
  steps {
    sh '''
      echo "🔍 Current directory"
      pwd

      echo "📂 Listing k8s directory"
      ls -l k8s/

      echo "📄 Applying backend deployment"
      kubectl apply -f k8s/backend-deployment.yaml

      echo "📄 Applying backend service"
      kubectl apply -f k8s/backend-service.yaml

      echo "📦 Deployments in default namespace"
      kubectl get deployments

      echo "🚀 Rollout status"
      kubectl rollout status deployment/backend
    '''
  }
}
