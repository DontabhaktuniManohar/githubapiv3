#!/bin/bash

# Define allowed ports
ALLOWED_PORTS=(8080 9090 7070)

# Get list of running ports and associated PIDs
RUNNING_PORTS=$(netstat -anp | grep LISTEN | awk '{print $4}' | awk -F: '{print $2}')

# Store incorrect PIDs
WRONG_PIDS=()

# Iterate over allowed ports
for PORT in "${ALLOWED_PORTS[@]}"; do
    # Get PID from ps command
    PS_PID=$(ps -ef | grep "$PORT" | grep LISTEN | awk '{print $2}')
    # Get PID from netstat command
    NETSTAT_PID=$(netstat -anp | grep "$PORT" | awk '{print $7}' | cut -d'/' -f1)
    
    # Compare PIDs
    # If both PIDs are missing, add to missing ports
    if [[ -z "$NETSTAT_PID" && -z "$PS_PID" ]]; then
        echo "No process found for port $PORT"
        MISSING_PORTS+=("$PORT")
    elif [[ -z "$NETSTAT_PID" || -z "$PS_PID" || "$NETSTAT_PID" != "$PS_PID" ]]; then
        echo "Incorrect or missing PID for port $PORT: netstat PID=$NETSTAT_PID, ps PID=$PS_PID"
        [[ -n "$NETSTAT_PID" ]] && WRONG_PIDS+=("$NETSTAT_PID")
        [[ -n "$PS_PID" ]] && WRONG_PIDS+=("$PS_PID")
        MISSING_PORTS+=("$PORT")
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
