# user_files.py

import os
import pwd
import sys

def list_user_files(directory, username):
    try:
        user_info = pwd.getpwnam(username)
        user_id = user_info.pw_uid

        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if os.stat(file_path).st_uid == user_id:
                    print(file_path)

    except KeyError:
        print(f"Error: User '{username}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python user_files.py <directory> <username>")
        sys.exit(1)

    directory = sys.argv[1]
    username = sys.argv[2]
    list_user_files(directory, username)
