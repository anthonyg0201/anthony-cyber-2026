# list_users.py

def list_users():
    try:
        with open('/etc/passwd', 'r') as file:
            for line in file:
                username = line.split(':')[0]
                print(username)
    except FileNotFoundError:
        print("Error: /etc/passwd file not found.")
    except PermissionError:
        print("Error: Permission denied when accessing /etc/passwd.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    list_users()
