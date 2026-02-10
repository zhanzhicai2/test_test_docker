pipeline {
    // agent any // 此时代理会使用已挂载Docker的Jenkins容器
    agent { node { label 'node-test' } } // 直接指定使用标签为node-test的节点
    // agent { node { label 'node-test-javaweb' } } // 直接指定使用标签为node-test-javaweb的节点
    tools {
        // 使用在Jenkins全局工具中配置的Allure命令行工具，名称需与你的配置一致
       allure 'Allure' 
     }
     options {
        quietPeriod(50) // 设置安静期为150秒，避免频繁触发构建
    }
    triggers {
        // 例如，这里可以保留你已有的GitHub Webhook或轮询SCM的触发器
        pollSCM('H/2 * * * *') // 每2分钟检查一次代码变更[7](@ref)
    }

    stages {
        stage('Checkout') {
            steps {
                // 检出代码
                checkout scm
                // hello world
                echo 'Hello World'
                echo "当前运行节点：${env.NODE_NAME}" // 打印节点名称，验证是否是Node-test
                echo "本机目录：${env.WORKSPACE}" // 打印本机目录，验证是否是Mac的Jenkins工作目录

            }
        }

        stage('Test') {
            steps {
                sh 'echo $PATH' // 查看代理进程的PATH
                sh 'which allure' // 查看代理进程能否找到allure
                sh '/usr/local/bin/allure --version' // 验证绝对路径是否可用
                sh 'python3 -V'
                sh 'pip3 -V'
                sh 'pip3 install -r requirements.txt'
                sh 'mkdir -p allure-results' // 确保目录存在
                sh 'ls -l allure-results' // 查看目录内容
                sh 'cd ./tests && python3 -m pytest test_main.py --alluredir=../allure-results --clean-alluredir' // 使用绝对路径存放Allure结果
            }
        }
        stage('Publish Allure Report') {
            // steps { // 关键步骤：发布Allure报告 node-test-javaweb node-test 本机MacBookpro获取报告方式
            //     // 手动生成报告
            //     sh '/usr/local/bin/allure generate ./allure-results -o ./allure-report --clean'
            //     // 第二步：归档报告文件（Jenkins原生步骤，无需插件）
            //     archiveArtifacts artifacts: 'allure-report/**/*', fingerprint: true
            //     // 第三步：仍用Allure插件发布（关键：在节点工具配置中指定Allure路径）
            //     script {
            //         // 手动指定Allure路径，覆盖插件的默认查找逻辑
            //         env.ALLURE_HOME = '/usr/local/bin'
            //     }
                // 发布HTML报告
                // publishHTML(
                //     target: [
                //         allowMissing: false,
                //         alwaysLinkToLastBuild: true,
                //         keepAll: true,
                //         reportDir: 'allure-report',
                //         reportFiles: 'index.html',
                //         reportName: 'Allure接口自动化测试报告'
                //     ]
                // )
                // 保留原Allure插件发布（可选）
            //     allure includeProperties: false, 
            //           jdk: '', 
            //           resultPolicy: 'LEAVE_AS_IS',
            //           results: [[path: "allure-results"]]
            // }
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
            echo 'Pipeline succeeded 运行在Mac的Node-test节点 你真厉害这都被你完成了，测试git提交代码测试设置，已经150s安静期'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
