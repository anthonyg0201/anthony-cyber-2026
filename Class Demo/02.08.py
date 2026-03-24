import socket

def check_ports(host, ports):
    """Checks if specific ports are open on a host."""
    for port in ports:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        
        # connect_ex returns 0 if the connection is successful
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"Port {port} on {host}: OPEN")
        else:
            print(f"Port {port} on {host}: CLOSED/FILTERED")
        
        sock.close()

if __name__ == "__main__":
    target = "127.0.0.1"  # localhost
    ports_to_check = [80, 443]
    
    print(f"Scanning {target}...")
    check_ports(target, ports_to_check)