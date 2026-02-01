pipeline {
    agent any // 此时代理会使用已挂载Docker的Jenkins容器

    stages {
        stage('Checkout') {
            steps {
                // 检出代码
                checkout scm
                // hello world
                echo 'Hello World'
            }
        }

        stage('Test') {
            steps {
                sh 'python -V'
                sh 'pip -V'
                sh 'pip install -r requirements.txt'
                sh 'cd ./tests && pytest test_main.py::test_health_check'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'Pipeline succeeded'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}