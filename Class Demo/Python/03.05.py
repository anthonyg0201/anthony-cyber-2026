# audit_files.py

import os
import stat

def find_world_writable_files(directory):
    try:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                file_stat = os.stat(filepath)
                if file_stat.st_mode & stat.S_IWOTH:
                    print(filepath)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = '/tmp'  # Change this to the desired directory
    find_world_writable_files(directory_path)