pipeline {
    agent any // 此时代理会使用已挂载Docker的Jenkins容器

    stages {
        stage('Initialize') {
            steps {
                // 直接验证，现在应该可以成功
                sh 'docker --version'
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-v $WORKSPACE:/workspace -w /workspace'
                    reuseNode true // 建议设为true，与Jenkins代理共享工作空间
                }
            }
            steps {
                sh 'python -V'
                sh 'pip -V'
                sh 'pip install -r requirements.txt'
                sh 'cd ./tests && pytest test_main.py::test_health_check'
            }
        }
    }
}