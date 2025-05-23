pipeline {
    agent any

    environment {
        EC2_HOST = "Demo@13.52.221.190>"
        PEM_FILE = "Demo-key.pem"  // Jenkins should have access to this file
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/pgakr992/EXAMPLE.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh """
                scp -i $PEM_FILE -o StrictHostKeyChecking=no app.py requirements.txt Dockerfile $EC2_HOST:/home/ec2-user/

                ssh -i $PEM_FILE -o StrictHostKeyChecking=no $EC2_HOST << 'EOF'
                    cd /home/ec2-user
                    docker build -t flask-app .
                    docker stop flask-container || true
                    docker rm flask-container || true
                    docker run -d -p 80:5000 --name flask-container flask-app
                EOF
                """
            }
        }
    }
}
