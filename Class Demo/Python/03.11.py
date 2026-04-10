# List Files in Directory

import os

def list_files_in_directory(directory_path):
    try:
        # List all files in the given directory
        for item in os.listdir(directory_path):
            file_path = os.path.join(directory_path, item)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                print(f"File: {item}, Size: {file_size} bytes")
    except FileNotFoundError:
        print("Error: The specified directory does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory = r"C:\Users\Unit 3 Lab 11"
list_files_in_directory(directory)

