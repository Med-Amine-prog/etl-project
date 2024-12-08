pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/Med-Amine-prog/etl-project.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run ETL') {
            steps {
                sh 'python scripts/extract.py'
                sh 'ls -la data/'
                sh 'python scripts/transform.py'
                sh 'ls -la data/'
                sh 'python scripts/load.py'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/test_etl.py --verbose'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker --version'
                    docker.build('etl-pipeline:latest')
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-credentials') {
                        docker.image('etl-pipeline:latest').push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline exécuté avec succès."
        }
        failure {
            echo "Pipeline échoué. Veuillez vérifier les logs."
        }
    }
}
