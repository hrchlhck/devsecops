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
    }

    post {
        always {
            // Limpar recursos após a execução
            sh 'rm -rf ./venv'
        }
    }
    
}
