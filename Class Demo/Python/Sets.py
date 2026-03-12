# List with Dups
logs = ["192.168.1.1","10.0.0.1","192.168.1.1"]

#Convert List to Set (Remove Dup)
unique_logs = set(logs)

#Print Unique logs
print("unique logs:", unique_logs)

# Create Another List of logs
logs2 = ["10.0.0.1","172.16.0.1"]

# Find Common ip (Using Set Intersection)
common_logs = unique_logs & set(logs2)

# Print Common logs
print("Common Logs:", common_logs)