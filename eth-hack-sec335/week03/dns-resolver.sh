#!/bin/bash
network=$1
dns_server=$2

echo "ip,hostname"
for i in $(seq 1 254); do
  ip="${network}.${i}"
  # reverse DNS lookup
  hostname=$(nslookup "$ip" "$dns_server" 2>/dev/null | grep 'name =' | awk '{print $NF}')

  # only output if a hostname was found
  if [ -n "$hostname" ]; then
    echo -e "$ip\t$hostname"
  fi
done
