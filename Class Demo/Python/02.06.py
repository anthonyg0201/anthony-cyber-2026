# Create a log filter that returns uniquely sorted IP's
def unique_sorted_ips(ip_list):
    return sorted(set(ip_list))

# Example usage
ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1"]
unique_ips = unique_sorted_ips(ips)
print(unique_ips)  # Output: ["10.0.0.1", "192.168.1.1", "192.168.1.1"]
