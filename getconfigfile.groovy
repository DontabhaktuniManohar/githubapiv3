pipeline {
    agent any

    stages {
        stage('Get Config XML') {
            steps {
                script {
                    def jobName = 'YourJobName'
                    def jobConfig = configFileProvider([configFile(fileId: jobName, variable: 'JOB_CONFIG')])

                    // Read the content of the config.xml file
                    def configXmlContent = jobConfig.toString()

                    // Print or process the config.xml content as needed
                    println "Config XML content for job $jobName:\n$configXmlContent"
                }
            }
        }
    }
}
