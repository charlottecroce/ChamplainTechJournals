#!/bin/sh
network=$1
port=$2

echo "host,port"
for i in $(seq 1 254); do
  host="${network}.${i}"
  timeout .1 bash -c "echo >/dev/tcp/$host/$port" 2>/dev/null &&
    echo "$host,$port"
done
