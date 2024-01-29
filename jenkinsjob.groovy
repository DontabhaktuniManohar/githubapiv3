def jobName = 'YourJobName'

def job = Jenkins.instance.getItemByFullName(jobName)
if (job) {
    def configXml = job.getConfigFile().getText()
    
    // Parse the XML to extract user names
    def userNames = []
    def xmlParser = new XmlParser()
    def configData = xmlParser.parseText(configXml)
    
    // Assuming users are defined in <authorizationMatrix> section
    def authorizationMatrix = configData['authorizationMatrix']
    if (authorizationMatrix) {
        authorizationMatrix['permission'].each { permission ->
            if (permission["@class"] == 'hudson.security.ProjectMatrixAuthorizationStrategy$ProjectMatrixEntry') {
                // Extract user names from permission definitions
                permission['user'].each { user ->
                    userNames.add(user.text())
                }
            }
        }
    }
    
    println "User names in $jobName job configuration: $userNames"
} else {
    println "Job '$jobName' not found."
}
