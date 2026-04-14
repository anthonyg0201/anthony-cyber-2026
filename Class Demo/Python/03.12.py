# list_services.py

import winreg
import subprocess

def list_running_services():
    try:
        services_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services')
        services_count = winreg.QueryInfoKey(services_key)[0]

        for i in range(services_count):
            service_name = winreg.EnumKey(services_key, i)
            service_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, fr'SYSTEM\CurrentControlSet\Services\{service_name}')
            try:
                display_name = winreg.QueryValueEx(service_key, 'DisplayName')[0]
                status = subprocess.check_output(f'sc query "{service_name}"', shell=True).decode()
                if "RUNNING" in status:
                    print(f'Service: {display_name} (Name: {service_name}) - Status: RUNNING')
                else:
                    print(f'Service: {display_name} (Name: {service_name}) - Status: NOT RUNNING')
            except Exception as e:
                print(f'Error accessing service {service_name}: {e}')
            finally:
                winreg.CloseKey(service_key)

        winreg.CloseKey(services_key)

    except PermissionError:
        print("Permission denied. Please run as Administrator.")
    except Exception as e:
        print(f'Error accessing services: {e}')

if __name__ == "__main__":
    list_running_services()
