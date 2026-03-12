# Create a csv log with IP's and then use this script to output IP's
import csv

with open('logs.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ip', 'time', 'status'])
    writer.writerow(['192.168.1.1', '12:01', '200'])
    writer.writerow(['192.168.1.2', '12:02', '404'])
    writer.writerow(['192.168.1.3', '12:03', '200'])

# Read CSV and print IPs
import csv

ips = []
with open('logs.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        ips.append(row[0])

print(f"IPs: {ips}")
