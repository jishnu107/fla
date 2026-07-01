pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from Git...'
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                // Jenkins will execute the appropriate command depending on the OS of the runner agent.
                // Here we use Windows batch syntax since the host is Windows.
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing requirements...'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running automated test cases with pytest...'
                bat 'venv\\Scripts\\pytest'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Build successful and all tests passed!'
        }
        failure {
            echo 'Build failed. Check test logs.'
        }
    }
}
