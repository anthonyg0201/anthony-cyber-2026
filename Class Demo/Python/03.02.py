# Directory Listing Script

import os

def list_directories(path):
    try:
        entries = os.listdir(path)
        directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
        for directory in directories:
            print(directory)
    except Exception as e:
        print(f"Error: {e}")

# Example usage
list_directories('/home')