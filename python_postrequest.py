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


##
import csv

# Sample dictionary data
data = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Bob', 'age': 35, 'city': 'Chicago'}
]

# Specify the CSV file path
csv_file_path = 'output.csv'

# Specify the field names (column names) for the CSV file
fieldnames = ['name', 'age', 'city']

# Write dictionary data to CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write rows
    for row in data:
        writer.writerow(row)

print("CSV file generated successfully.")

###################
import csv

# Define the CSV file path
csv_file_path = 'your_file.csv'

# Sample dictionary with keys for the new header
new_header_dict = {'name': 'Name', 'age': 'Age', 'city': 'City'}

# Read the existing CSV file
with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Update the header row with the new keys
rows[0] = list(new_header_dict.values())

# Write the updated data back to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV header updated successfully.")

##############
import csv

# Define the CSV file path
csv_file_path = 'your_file.csv'

# Sample dictionary with keys and corresponding new values
update_values_dict = {'name': 'John Doe', 'age': '35'}

# Row index where you want to update values (0-based index)
row_index_to_update = 1  # For example, update the second row

# Read the existing CSV file
with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Get the header row to map keys to column indexes
header_row = rows[0]
key_to_column_index = {key: header_row.index(key) for key in update_values_dict}

# Update values in the specified row based on keys
for key, value in update_values_dict.items():
    column_index = key_to_column_index.get(key)
    if column_index is not None:
        rows[row_index_to_update][column_index] = value

# Write the updated data back to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV row updated successfully.")
############
