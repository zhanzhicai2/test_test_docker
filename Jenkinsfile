// pipeline {
//     agent any // 此时代理会使用已挂载Docker的Jenkins容器
//     // tools {
//     //     // 使用在Jenkins全局工具中配置的Allure命令行工具，名称需与你的配置一致
//     //    allure 'Allure' 
//     // }

//     stages {
//         stage('Checkout') {
//             steps {
//                 // 检出代码
//                 checkout scm
//                 // hello world
//                 echo 'Hello World'
//             }
//         }

//         stage('Test') {
//             steps {
//                 sh 'python -V'
//                 sh 'pip -V'
//                 sh 'pip install -r requirements.txt'
//                 // sh 'mkdir -p allure-results' // 确保目录存在
//                 // sh 'cd ./tests && python3 -m pytest test_main.py --alluredir=./allure-results --clean-alluredir'
//                 sh 'cd ./tests &&python3 -m pytest test_main.py'
//             }
//         }
//         // stage('Publish Allure Report') {
//         //     steps {
//         //         // 关键步骤：发布Allure报告
//         //         allure includeProperties: false, 
//         //               jdk: '', 
//                          resultPolicy: 'LEAVE_AS_IS',
//         //               results: [[path: "$WORKSPACE/allure-results"]] // 使用绝对路径, 此路径需与--alluredir参数指定的路径一致
//         //     }
//         // }
//     }
    
//     post {
//         always {
//             echo 'Pipeline finished'
//             // 始终发送邮件，但根据状态不同会有不同的处理
//             emailext (
//                 subject: "'${env.JOB_NAME} - Build # ${env.BUILD_NUMBER} - ${currentBuild.currentResult}!'",
//                 body: '${DEFAULT_CONTENT}', // 使用系统配置的默认内容
//                 to: '1610893869@qq.com', // 可以在这里指定收件人，如: 'team@example.com'
//                 mimeType: 'text/html'
//             )
//         }
//         success {
//             echo 'Pipeline succeeded'
//         }
//         failure {
//             echo 'Pipeline failed'
//         }
//     }
// }

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
                sh 'mkdir -p allure-results' // 确保目录存在
                sh 'ls -l allure-results' // 查看目录内容
                sh 'cd ./tests && python3 -m pytest test_main.py'
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
                to: '1610893869@qq.com', // 可以在这里指定收件人，如: 'team@example.com'
                mimeType: 'text/html'
            )
        }
        success {
            echo 'Pipeline succeeded'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}