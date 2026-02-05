pipeline {
    agent any // 此时代理会使用已挂载Docker的Jenkins容器
    tools {
        // 使用在Jenkins全局工具中配置的Allure命令行工具，名称需与你的配置一致
       allure 'Allure' 
     }
     options {
        quietPeriod(300)
    }
    triggers {
        // 例如，这里可以保留你已有的GitHub Webhook或轮询SCM的触发器
        pollSCM('H/5 * * * *') // 每5分钟检查一次代码变更[7](@ref)
    }

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
                sh 'mkdir -p allure-results' // 确保目录存在
                sh 'ls -l allure-results' // 查看目录内容
                sh 'cd ./tests && python3 -m pytest test_main.py --alluredir=../allure-results --clean-alluredir' // 使用绝对路径存放Allure结果
            }
        }
        stage('Publish Allure Report') {
            steps {
                // 关键步骤：发布Allure报告
                allure includeProperties: false, 
                      jdk: '', 
                         resultPolicy: 'LEAVE_AS_IS',
                      results: [[path: "allure-results"]] // 使用绝对路径, 此路径需与--alluredir参数指定的路径一致
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished'
            // 始终发送邮件，但根据状态不同会有不同的处理
            emailext (
                subject: "'${env.JOB_NAME} - Build # ${env.BUILD_NUMBER} - ${currentBuild.currentResult}!'",
                body: '${DEFAULT_CONTENT}', // 使用系统配置的默认内容
                to: '161089@qq.com', // 可以在这里指定收件人，如: 'team@example.com'
                mimeType: 'text/html'
            )
        }
        success {
            echo 'Pipeline succeeded 你真厉害这都被你完成了，测试git提交代码测试'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
