pipeline{
    agent any

    stages {
        stage('Checkout'){
            steps {
                git branch: 'main', credentialsId: 'github-credentials-id', url: 'https://github.com/Muhammadjunaid7864/hashicorp_kv_tf.git'
            }
        }
        stage('install requirements '){
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Flask project'){
            steps{
                bat 'flask run'
            }
        }
    }
}