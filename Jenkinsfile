pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clonar o repositório do código-fonte
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                // Configurar ambiente virtual Python
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Executar testes da aplicação
                sh '. venv/bin/activate && python -m unittest discover'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t hrchlhck/devsecops .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'if [[ $(docker ps --format "{{.Names}}") == *"teste"* ]]; then docker kill teste; fi'
                sh 'docker run -d -p 8888:8080 --name teste --rm hrchlhck/devsecops'
            }
        }
    }

    post {
        always {
            // Limpar recursos após a execução
            sh 'rm -rf ./venv'
        }
    }
    
}
