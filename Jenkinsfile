pipeline {
    // 不在顶层指定全局agent，允许每个stage灵活定义
    agent none
    stages {
        tage('Initialize') {
            steps {
                script {
                    // 获取自动安装的Docker工具的路径，并将其添加到环境变量PATH中
                    def dockerHome = tool 'my-docker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
                // 验证Docker命令是否可用
                sh 'docker --version'
            }
        }
        
        stage('Checkout') {
            agent {
                docker {
                    // 使用一个包含git等基础工具的小型镜像来拉取代码，可以提升效率
                    image 'alpine/git:2.42.0'
                    // 将仓库代码挂载到容器内，args参数会传递给`docker run`
                    args '-v /path/to/workspace/on/host:/workspace -w /workspace'
                }
            }
            steps {
                // 拉取代码。使用SCM关键字会自动拉取当前Jenkins任务配置的仓库和分支。
                checkout scm
            }
        }
        
        
        stage('Test') {
            agent {
                docker {
                    // 指定包含Python 3.11环境的官方镜像
                    image 'python:3.11'
                    // 可以指定容器内的工作目录。如果不需要复用缓存，仅-w参数即可。
                    args '-v $WORKSPACE:/workspace -w /workspace'
                    // 每个stage都在全新的容器中运行[2](@ref)
                    reuseNode false
                }
            }
            steps {
                // 你原有的shell脚本命令，现在将在python:3.11容器内执行
                sh 'python -V'
                sh 'pip -V'
                sh 'pip install -r requirements.txt'
                sh 'cd ./tests && pytest test_main.py::test_health_check'
            }
        }
    }
}