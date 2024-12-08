pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install --upgrade pip'
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
