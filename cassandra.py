#pip install cassandra-driver

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
