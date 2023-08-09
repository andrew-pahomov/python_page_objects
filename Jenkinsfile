#!groovy
node {
    def build_ok = true
        stage("Prepare") {
            sh 'chmod +x gradlew'
            sh 'java -jar ./artifacts/app-ibank-build-for-testers.jar &'
        }
    try{
        stage('Run tests') {
            sh 'pytest'
        }
    } catch(e) {
        build_ok = false
        echo e.toString()
    }
    if(build_ok) {
        currentBuild.result = "SUCCESS"
    } else {
        currentBuild.result = "FAILURE"
    }
}