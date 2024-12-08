pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/Med-Amine-prog/etl-project.git' // Remplacez par l'URL de votre repo
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('etl-pipeline:latest') // Construire l'image Docker basée sur le Dockerfile du projet
                }
            }
        }
        stage('Run ETL') {
            agent {
                docker {
                    image 'etl-pipeline:latest' // Utiliser l'image Docker construite
                }
            }
            steps {
                sh 'python scripts/extract.py' // Exécuter les scripts ETL
                sh 'python scripts/transform.py'
                sh 'python scripts/load.py'
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
