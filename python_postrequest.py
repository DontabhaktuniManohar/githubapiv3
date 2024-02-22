from flask import Flask, request

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def handle_post_request():
    if request.method == 'POST':
        # Get the data from the POST request
        data = request.json  # Assuming the data is sent in JSON format

        # Process the data
        # For example, print the data received
        print("Received data:", data)

        # Return a response
        return 'Data received successfully', 200
    else:
        return 'Only POST requests are allowed', 405

if __name__ == '__main__':
    app.run(debug=True)

###
import requests

url = 'http://localhost:5000/endpoint'
data = {'key': 'value'}  # Data to be sent in JSON format

response = requests.post(url, json=data)

print(response.text)  # Print the response from the server
