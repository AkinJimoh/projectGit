pipeline {
    agent any
    parameters {
        string(name: "TEST_STRING", defaultValue: "DEV", trim: true, description: "Sample string parameter")
        choice(name: "TEST_CHOICE", choices: ["production", "staging", "development"], description: "Sample multi-choice parameter")
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
                bash one/two/main.sh
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