pipeline {
    agent any

    stages {
        stage('Extract Users List') {
            steps {
                script {
                    def jobName = 'YourJobName'
                    def configFile = readFile("${JENKINS_HOME}/jobs/${jobName}/config.xml")

                    // Parse the config.xml content
                    def configXml = new XmlSlurper().parseText(configFile)

                    // Extract user names
                    def userNames = []

                    // Assuming users are defined in the <authorizationMatrix> section
                    configXml.authorizationMatrix.each { permission ->
                        if (permission["@class"] == 'hudson.security.ProjectMatrixAuthorizationStrategy$ProjectMatrixEntry') {
                            // Extract user names from permission definitions
                            permission.user.each { user ->
                                userNames.add(user.text())
                            }
                        }
                    }

                    println "User names in $jobName job configuration: $userNames"
                }
            }
        }
    }
}
