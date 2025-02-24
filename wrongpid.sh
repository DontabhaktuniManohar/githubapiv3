#!/bin/bash

# Define allowed ports
ALLOWED_PORTS=(8080 9090 7070)

# Get list of running ports and associated PIDs
RUNNING_PORTS=$(netstat -anp | grep LISTEN | awk '{print $4 " " $7}' | awk -F: '{print $2 " " $3}')

# Store incorrect PIDs
WRONG_PIDS=()

# Iterate over running ports
while read -r PORT PID; do
    if [[ ! " ${ALLOWED_PORTS[@]} " =~ " ${PORT} " ]]; then
        echo "Port $PORT is not allowed. Process ID: $PID"
        WRONG_PIDS+=("$PID")
    fi
done <<< "$RUNNING_PORTS"

# Kill incorrect PIDs
for PID in "${WRONG_PIDS[@]}"; do
    if [[ -n "$PID" ]]; then
        echo "Killing process $PID"
        kill -9 "$PID"
    fi
done

# Start JVMs
echo "Starting JVMs..."
# Update the command below to match your JVM startup script or command
nohup java -jar /path/to/your/application.jar &

echo "JVMs started."
