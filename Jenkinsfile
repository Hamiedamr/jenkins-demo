pipeline{
    agent any
    environment {
        dockerImage=''
        registry = 'abdelhamiedamr/jenkins-demo'
        registryCredential='abdelhamiedamr_id'
    }
        stages {
            stage('Checkout'){
                steps {
                    checkout scmGit(branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Hamiedamr/jenkins-demo']])
                    bat 'pip install -r requirements.txt'
                    bat 'pytest app'
    
                }
            }
            stage('Build Docker Image') {
                steps {
                    script {
                        dockerImage= docker.build registry
                    }
                }
            }
            stage('Push Docker Image to Docker Hub') {
                steps {
                    script {
                        docker.withRegistry('',registryCredential){
                            dockerImage.push()
                        }
                    }
                }
            }
        }
    }