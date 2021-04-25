pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                sh "python --version"
                echo 'Python have been installed'
            }
        }
        stage('Git') {
            steps {
                git branch: 'develop',
                    url: 'https://github.com/alexey-malashenko/ci_cd',
                    credentialsId: 'jenkins_ssh_key'
                echo 'Git have been cloned'
            }
        }
        stage('Python env') {
            steps {
                sh "python main.py"
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                echo "Running ${env.BUILD_ID} ${env.BUILD_DISPLAY_NAME} on ${env.NODE_NAME} and JOB ${env.JOB_NAME}"
            }
        }
        stage('List') {
            steps{
                sh("dir ${JENKINS_HOME}")
            }
        }
        stage('Тестирование') {
            steps {
                sh 'git config --global user.email "alexey_malashenko@epam.com"'
                sh 'git config --global user.name "alexey-malashenko"'
            }
        }
        stage('Развертывание') {
            steps {
                echo 'Переносим код в рабочую среду или создаем артефакт'
            }
        }
    }
}