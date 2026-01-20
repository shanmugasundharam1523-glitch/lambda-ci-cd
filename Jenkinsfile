stage('Package Lambda') {
    steps {
        sh '''
        echo "PWD:"
        pwd
        echo "Files in workspace:"
        ls -l

        zip -r function.zip lambda_function.py

        echo "Zip file details:"
        ls -lh function.zip
        '''
    }
}
