pipeline {
    agent any // 此时代理会使用已挂载Docker的Jenkins容器

    stages {
        stage('Checkout') {
            steps{
                // hello world
                echo 'Hello World'
            }
            steps {
                // 检出代码
                checkout scm
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
}