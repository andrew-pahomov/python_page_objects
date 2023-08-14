#!groovy
pipeline {
    agent any

    stages {
        stage("Prepare") {
            steps {
                sh 'java -jar ./artifacts/app-ibank-build-for-testers.jar &'
                sleep time: 5000, unit: 'MILLISECONDS'
            }
        }

        stage("Run tests") {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'python3.11 -m pytest --alluredir=./allure-report'
                }
            }
        }

        stage("Generate Reports") {
            steps {
                allure ([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: './allure-report']]
                ])
            }
        }
    }
}