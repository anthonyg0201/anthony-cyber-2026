# Create a Program to check Ports 80,443 on localhost
import socket

def check_ports(host, ports):
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            # Set a time Out
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open on {host}.")
            else:
                print(f"Port {port} is closed on {host}.")

if __name__ == "__main__":
    host = "localhost"
    ports_to_check = [80, 443]
    check_ports(host, ports_to_check)