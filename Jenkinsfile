pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Med-Amine-prog/etl-project.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run ETL') {
            steps {
                sh 'python scripts/extract.py'
                sh 'python scripts/transform.py'
                sh 'python scripts/load.py'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/test_etl.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('etl-pipeline:latest')
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', '58a00dd7-a0ce-4b1c-8d25-8dab2db1ca94') {
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
