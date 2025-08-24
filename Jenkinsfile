pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'tbendr/getuser'
        HELM_RELEASE = 'getuser'
        K8S_NAMESPACE = 'default'
        DOCKER_REGISTRY_CREDS = 'docker-hub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/tomer-bdbd/DevOpsCourse.git'
            }
        }
        
        stage('Build') {
            steps {
                script {
                    dir('getuser') {
                        sh "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} -f Dockerfile ."
                    }
                    
                    env.IMAGE_TAG = BUILD_NUMBER
                    withCredentials([usernamePassword(credentialsId: env.DOCKER_REGISTRY_CREDS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin && docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                    }
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Hello Test'
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    sh 'kubectl cluster-info'
                    
                    // If release already exists, upgrade. Otherwise install.
                    def releaseExists = sh(
                        script: "helm list -n ${K8S_NAMESPACE} -q | grep -q '^${HELM_RELEASE}\$'",
                        returnStatus: true
                    )
                    
                    if (releaseExists == 0) {
                        echo 'Release exists, upgrading...'
                        sh """
                            helm upgrade ${HELM_RELEASE} ./getuser-0.1.0.tgz \
                                --namespace ${K8S_NAMESPACE} \
                                --set image.tag=${IMAGE_TAG} \
                                --wait --timeout=300s
                        """
                    } else {
                        echo 'Release does not exist, installing...'
                        sh """
                            helm install ${HELM_RELEASE} ./getuser-0.1.0.tgz \
                                --namespace ${K8S_NAMESPACE} \
                                --set image.tag=${IMAGE_TAG} \
                                --create-namespace \
                                --wait --timeout=300s
                        """
                    }
                }
            }
        }
    }
}
