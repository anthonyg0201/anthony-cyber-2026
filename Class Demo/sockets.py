# Import the socket Module (Library)
import socket

# Create TCP Socket
s = socket.socket()

# Set a time Out
s.settimeout(1)

#Connect to a Port
result = s.connect_ex(("localhost", 80))

# Print the Results
print("Port Open" if result == 0 else "Port Closed")

# Close The socket
s.close()