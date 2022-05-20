pipeline {
    agent any
    parameters {
        string(name: "TEST_STRING", defaultValue: "main", trim: true, description: "Sample string parameter")
        choice(name: "TEST_CHOICE", choices: ["production", "staging", "development"], description: "Sample multi-choice parameter")
    }
    stages {
        stage("Build") {
            steps {
                echo "Build stage."
                echo "Hello $params.TEST_STRING"
                sh """
                pwd
                ls -lah
                python3 -V
                """
            }
        }
        stage("Test") {
            steps {
                echo "Test stage."
                sh """
                chmod +x main.sh
                ./main.sh
                """
            }
        }
        stage("Release") {
            steps {
                echo "Release stage."
            }
        }
    }
}