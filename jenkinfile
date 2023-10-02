pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'fd80a6af-9cc0-432a-91a3-d05882601c2c', url: 'https://github.com/cloudtechtrainer/B2-DevOps-Jenkins-EC2.git']])
            }
        }
        
        stage('Check Dependencies') {
            steps {
                sh '''
                        python3 app.py 3 4 add
                    '''
            }
        }
        
        stage('Run and Validate Tests') {
            steps {
                script {
                    def output
                    def expected

                    // Test 1: Add
                    output = sh(script: 'python3 app.py 3 4 add', returnStdout: true).trim()
                    expected = 'Result is  7.0'
                    if (output == expected) {
                        echo "Add test passed"
                    } else {
                        error "Add test failed"
                    }

                    // Test 2: Subtract
                    output = sh(script: 'python3 app.py 9 3 sub', returnStdout: true).trim()
                    expected = 'Result is  6.0'
                    if (output == expected) {
                        echo "Subtract test passed"
                    } else {
                        error "Subtract test failed"
                    }

                    // Test 3: Multiply
                    output = sh(script: 'python3 app.py 2 3 mul', returnStdout: true).trim()
                    expected = 'Result is  6.0'
                    if (output == expected) {
                        echo "Multiply test passed"
                    } else {
                        error "Multiply test failed"
                    }

                    // Test 4: Divide
                    output = sh(script: 'python3 app.py 8 2 div', returnStdout: true).trim()
                    expected = 'Result is  4.0'
                    if (output == expected) {
                        echo "Divide test passed"
                    } else {
                        error "Divide test failed"
                    }
                }
            }
        }
    }
}
