pipeline {
    agent any
    parameters {
        // string(name: "TEST_STRING", defaultValue: "DEV", trim: true, description: "Sample string parameter")
        choice(name: "TEST_STRING", choices: ["SIT", "DEV", "PROD", "TEST"], description: "Sample multi-choice parameter")
    }
    stages {
        stage("Build") {
            steps {
                sh """
                pwd
                ls -lah
                python3 main.py
                """
            }
        }
        stage("Test") {
            steps {
                echo "Test stage."
                sh """
                bash main.sh
                """
            }
        }
        stage("Release") {
            steps {
                echo "Release stage."
            }
        }
    }
        post {
            // Clean after build
            always {
                cleanWs()
            }
        }
    }