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


def jenkinsUrl = 'http://your-jenkins-url'
def jobName = 'YourJobName'

def configXml

// Make HTTP GET request to retrieve the job configuration XML
def url = "${jenkinsUrl}/job/${jobName}/config.xml"
def connection = url.toURL().openConnection()
connection.setRequestMethod('GET')

try {
    configXml = connection.inputStream.text
} finally {
    connection.inputStream.close()
}

// Process the config.xml content as needed
println "Config XML content for job $jobName:\n$configXml"
