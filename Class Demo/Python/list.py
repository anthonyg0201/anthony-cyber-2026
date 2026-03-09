#list.py
#Create a list of IP addresses
ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1", "192.168.1.1", "10.0.0.1"]

# Add another IP to the list
ips.append("172.16.0.2")
print("All IPs:", ips)

# Access elements by index
print("First IP:"), ips[0]

#Slice the list
print("First two IPs:", ips[0:2])

# Remove an IP
ips.remove("10.0.0.1")
print("After removal:", ips)

# Sort the list
ips.sort()
print("Sorted IPs:", ips)

#List comprehension: filter IPs containing '192'
filtered_ips = [ip for ip in ips if "192" in ip]
print("Filtered IPs:", filtered_ips)

# List comprehension: double each item in a numeric example
numbers = [1, 2, 3, 4]
doubled = [x * 2 for x in numbers]
print("Doubled numbers:", doubled)

# Function to find duplicate IPs
def find_duplicates(ips_list):
    seen =set()
    duplicates = set()
    for ip in ips_list:
        if ip in seen:
            duplicates.add(ip)
        else:
            seen.add(ip)
    if duplicates:
        print("Duplicate IPs found:", duplicates)
    else:
        print("No duplicates found.")

# Test the function
find_duplicates(ips)


# Example of index error
# print(ips)[10]  # Uncommenting this will raise IndexError

