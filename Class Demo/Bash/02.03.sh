#!/bin/bash

check_port() {
  nc -z "$1" "$2" &>/dev/null
  if [ $? -eq 0 ]; then
    echo "open"
  else
    echo "closed"
  fi
}

host="127.0.0.1"
ports=(80 443 22)

for port in "${ports[@]}"; do
  status=$(check_port "$host" "$port")
  echo "Port $port is $status"
done

