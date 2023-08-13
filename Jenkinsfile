#!groovy
node {
    def build_ok = true
        stage("Prepare") {
            sh 'java -jar ./artifacts/app-ibank-build-for-testers.jar &'
        }
    try{
        stage('Run tests') {
            sh 'python3.11 -m pytest'
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