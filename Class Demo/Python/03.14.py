# system_info.py

import winreg

def get_os_info():
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion')
        os_name = winreg.QueryValueEx(registry_key, 'ProductName')[0]
        os_version = winreg.QueryValueEx(registry_key, 'CurrentVersion')[0]
        winreg.CloseKey(registry_key)
        
        print(f"Operating System: {os_name}")
        print(f"Version: {os_version}")
    except Exception as e:
        print(f"Error accessing registry: {e}")

if __name__ == "__main__":
    get_os_info()
