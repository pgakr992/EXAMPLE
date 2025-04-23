pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourname/flask-app.git'
            }
        }

        stage('Build & Run') {
            steps {
                sh 'docker build -t flask-app .'
                sh 'docker run -d -p 5000:5000 --name flask-app flask-app'
            }
        }
    }
}
