pipeline {
    agent any
    environment {
        IMAGE_NAME = "paoulo/csy3056-flask-app"
        REGISTRY_CREDENTIALS = "dockerhub-creds"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh 'flake8 app'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/ --cov=app'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def commit = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    docker.build("${IMAGE_NAME}:${commit}")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                withDockerRegistry(credentialsId: REGISTRY_CREDENTIALS) {
                    script {
                        def commit = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                        docker.image("${IMAGE_NAME}:${commit}").push()
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl rollout status deployment/flask-app'
            }
        }
    }
    post {
        always {
            junit 'pytest-report.xml'
            archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
        }
    }
}
