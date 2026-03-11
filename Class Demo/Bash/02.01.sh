#!/bin/bash

# 1. Store name in a variable
username="Anthony"

# 2. Print a greeting
echo "Hello, $username!"

# 3. Check if /var/log/syslog exists
if [[ -f "/var/log/syslog" ]];then
    echo "Syslog found!"
else
    echo "Syslog missing!"
fi