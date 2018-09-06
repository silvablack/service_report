node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image service') {
        app = docker.build("silvablack/service_report")
    }

    stage('RUN image'){
        app.run()
    }

    stage('Test unit'){
        app.inside{
            sh 'echo \"Test Unit\"'
            sh 'pytest test-unit-controllers.py'
        }
    }
    
    stage('Login ECR') {
        sh("eval \$(aws ecr get-login --no-include-email | sed 's|https://||')")
    }

    stage('Send repository') {
        docker.withRegistry('666829565535.dkr.ecr.us-east-2.amazonaws.com/aws-ecr-api-report', 'ecr:us-east-1:ecr-credentials'){
            app.image().push('latest')
        }
    }

}
