# check_perms.py

import os
import stat

def check_file_permissions(directory):
    try:
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                permissions = stat.filemode(os.stat(file_path).st_mode)
                print(f"{file}: {permissions}")
    except FileNotFoundError:
        print("Invalid path. Please check the directory and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    check_file_permissions(directory_path)
