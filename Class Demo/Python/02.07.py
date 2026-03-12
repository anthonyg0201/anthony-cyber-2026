# Create Users with a connected IP address
users = {"alice": {"ip": "192.168.1.1", "login": "2025-06-20"}}

# Print users and IPs
for user, details in users.items():
    print(f"{user}: {details['ip']}")