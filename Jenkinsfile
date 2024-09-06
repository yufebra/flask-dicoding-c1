pipeline {
    agent {
        docker {
            image 'python:latest'
            args '-v /tmp/cache:/pip-cache'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python -m venv venv'
                sh './venv/bin/activate && pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'python -m flask run --port=5000'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }
    }
}