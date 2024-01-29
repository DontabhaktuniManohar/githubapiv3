import requests
from requests.auth import HTTPBasicAuth

def get_users_list(jenkins_url, job_name, username, api_token):
    # Jenkins job config.xml API endpoint
    config_xml_url = f"{jenkins_url}/job/{job_name}/config.xml"

    # Make a GET request to the config.xml endpoint
    response = requests.get(config_xml_url, auth=HTTPBasicAuth(username, api_token))

    # Check if the request was successful
    if response.status_code == 200:
        # Extract user information from the XML response
        users = []
        for line in response.text.split('\n'):
            if 'authenticated' in line:
                user = line.split()[2].strip()
                users.append(user)
        return users
    else:
        # Print error message if request failed
        print(f"Failed to retrieve job configuration. Status code: {response.status_code}")
        return None

# Jenkins server details
jenkins_url = 'http://your-jenkins-url'
username = 'your_username'
api_token = 'your_api_token'

# Jenkins job details
job_name = 'YourJobName'

# Retrieve users list from Jenkins job configuration
users_list = get_users_list(jenkins_url, job_name, username, api_token)
if users_list:
    print(f"Users who accessed the job '{job_name}': {users_list}")
else:
    print("Failed to retrieve users list.")
