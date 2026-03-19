# Create a Log entry
log = "IP: 192.168.1.1, Time: 2025-06-20"

# Split the string into parts
parts = log.split(",")

# Print the first part
print("First Part:", parts[0])

# Remove "IP:" Form String
ip = parts[0].replace("IP: ", "")

# Print Clean IP
print("IP address:", ip)

# Optional: Remove extra spaces
IP = parts[0].replace("IP: ", "").strip()

print("IP address (stripped):", IP)