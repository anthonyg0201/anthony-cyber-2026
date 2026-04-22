import socket
from datetime import datetime
import sys

def get_vm_ip():
    """Gets the primary IPv4 address of the VM."""
    try:
        # Get hostname
        hostname = socket.gethostname()
        # Get IP address associated with the hostname
        ip_address = socket.gethostbyname(hostname)
        
        # Get current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Print output
        print(f"[{timestamp}] VM IPv4 Address: {ip_address}")
        
    except socket.gaierror as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: Could not resolve hostname. {e}")
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Unexpected Error: {e}")

if __name__ == "__main__":
    get_vm_ip()
