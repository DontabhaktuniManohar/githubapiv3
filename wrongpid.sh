#!/bin/bash

# Define allowed ports
ALLOWED_PORTS=(8080 9090 7070)

# Get list of running ports and associated PIDs
RUNNING_PORTS=$(netstat -anp | grep LISTEN | awk '{print $4}' | awk -F: '{print $2}')

# Store incorrect PIDs
WRONG_PIDS=()

# Iterate over running ports
for PORT in $RUNNING_PORTS; do
    PID=$(ps -ef | grep "$PORT" | grep -v grep | awk '{print $2}')
    if [[ ! " ${ALLOWED_PORTS[@]} " =~ " ${PORT} " ]]; then
        echo "Port $PORT is not allowed. Process ID: $PID"
        WRONG_PIDS+=("$PID")
    fi
done

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
