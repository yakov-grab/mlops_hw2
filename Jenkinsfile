pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Data Creation') {
            steps {
                script {
                    sh 'python3 src/data_creation.py'
                }
            }
        }
        stage('Model Preprocessing') {
            steps {
                script {
                    sh 'python3 src/model_preprocessing.py'
                }
            }
        }
        stage('Model Preparation') {
            steps {
                script {
                    sh 'python3 src/model_preparation.py'
                }
            }
        }
        stage('Model Testing') {
            steps {
                script {
                    sh 'python3 src/model_testing.py'
                }
            }
        }
    }
}
