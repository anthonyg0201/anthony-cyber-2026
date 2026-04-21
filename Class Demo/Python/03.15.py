# list_users.py

import winreg

def list_local_users():
    try:
        registry_path = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList'
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path) as key:
            for i in range(winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                with winreg.OpenKey(key, subkey_name) as subkey:
                    username = winreg.QueryValueEx(subkey, 'ProfileImagePath')[0].split('\\')[-1]
                    print(username)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_local_users()
