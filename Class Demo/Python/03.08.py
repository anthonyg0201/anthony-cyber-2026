# suid_files.py

import os
import stat

def list_suid_files(directory):
    try:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.isfile(filepath):
                    file_stat = os.stat(filepath)
                    if file_stat.st_mode & stat.S_ISUID:
                        print(filepath)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = '/usr/bin'  # Change this to the desired directory
    list_suid_files(directory_path)
