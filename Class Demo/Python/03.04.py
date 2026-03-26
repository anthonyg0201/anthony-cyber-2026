# List Files with Specific Extension

import os

def list_files_with_extension(directory, extension):
    try:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(extension):
                    full_path = os.path.join(dirpath, filename)
                    print(full_path)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
list_files_with_extension('/home', '.txt')