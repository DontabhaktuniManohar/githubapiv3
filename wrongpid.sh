#!/bin/bash

# Define allowed ports
declare -A PORT_SCRIPTS
PORT_SCRIPTS=(
    [8080]="/path/to/script_8080.sh"
    [9090]="/path/to/script_9090.sh"
    [7070]="/path/to/script_7070.sh"
)
# Store incorrect PIDs
WRONG_PIDS=()
# Store missing ports
MISSING_PORTS=()


# Iterate over allowed ports
for PORT in "${!PORT_SCRIPTS[@]}"; do
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

# Display missing ports
if [[ ${#MISSING_PORTS[@]} -gt 0 ]]; then
    echo "Missing ports: ${MISSING_PORTS[*]}"
fi

# Start JVMs using corresponding scripts
for PORT in "${MISSING_PORTS[@]}"; do
    if [[ -n "${PORT_SCRIPTS[$PORT]}" ]]; then
        echo "Starting service for port $PORT using script ${PORT_SCRIPTS[$PORT]}"
        nohup bash "${PORT_SCRIPTS[$PORT]}" &
    else
        echo "No startup script defined for port $PORT"
    fi
done

# Start JVMs
echo "Starting JVMs..."
# Update the command below to match your JVM startup script or command
nohup java -jar /path/to/your/application.jar &

echo "JVMs started."
