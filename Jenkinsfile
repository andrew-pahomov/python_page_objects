#!groovy
pipeline {
    agent any
    stages {
        stage("Prepare") {
            steps {
                sh 'java -jar ./artifacts/app-ibank-build-for-testers.jar &'
            }
        }
        stage("Run tests") {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'python3.11 -m pytest'
                }
            }
        }
    }
}