# Extract IP's from a log string (e.g., "Error from 192.168.1.1").
import re

log_string = "Error from 192.168.1.1"
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ips = re.findall(ip_pattern, log_string)

for ip in ips:
    print(f"IP: {ip}")