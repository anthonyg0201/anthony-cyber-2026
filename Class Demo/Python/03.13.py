# log_times.py

import os
import datetime

def list_log_files(directory):
    try:
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                modification_time = os.path.getmtime(file_path)
                formatted_time = datetime.datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
                print(f"{file}: {formatted_time}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = r"C:\Windows\Logs"
    list_log_files(directory_path)
