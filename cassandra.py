i#pip install cassandra-driver

from cassandra.cluster import Cluster
import json



# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])  # Replace with your Cassandra cluster's IP address
session = cluster.connect('your_keyspace')  # Replace 'your_keyspace' with your actual keyspace

# Read JSON file
with open('data.json', 'r') as f:
    json_data = json.load(f)

# Define your table's schema and column names
table_name = 'your_table'
columns = ['column1', 'column2', 'column3']  # Replace with your column names

# Insert or update data into the table
for item in json_data:
    values = [item.get(col) for col in columns]
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(columns))})"
    session.execute(query, values)

# Close connection
cluster.shutdown()


####
from flask import Flask, render_template
from cassandra.cluster import Cluster

app = Flask(__name__)

# Connect to Cassandra
cluster = Cluster(['localhost'])  # Replace 'localhost' with your Cassandra host
session = cluster.connect('your_keyspace')  # Replace 'your_keyspace' with your keyspace name

@app.route('/')
def index():
    # Query Cassandra to retrieve column names
    keyspace_name = 'your_keyspace'  # Replace 'your_keyspace' with your keyspace name
    table_name = 'your_table'  # Replace 'your_table' with your table name
    column_rows = session.execute(f"SELECT column_name FROM system_schema.columns WHERE keyspace_name='{keyspace_name}' AND table_name='{table_name}'")
    
    # Extract column names from rows
    column_names = [row.column_name for row in column_rows]

    # Query Cassandra for data
    data_rows = session.execute(f'SELECT * FROM {keyspace_name}.{table_name}')
    
    # Convert data rows to a list of dictionaries for easier manipulation in the HTML template
    data = [{col: getattr(row, col) for col in column_names} for row in data_rows]
    
    # Render HTML template with data
    return render_template('index.html', data=data, column_names=column_names)

if __name__ == '__main__':
    app.run(debug=True)


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data from Cassandra</title>
</head>
<body>
    <h1>Data from Cassandra</h1>
    <table>
        <tr>
            {% for column in column_names %}
            <th>{{ column }}</th>
            {% endfor %}
        </tr>
        {% for row in data %}
        <tr>
            {% for column in column_names %}
            <td>{{ row[column] }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>
</body>
</html>

