# list_group.py

def list_group_members(group_name):
    try:
        with open('/etc/group', 'r') as file:
            for line in file:
                if line.startswith(group_name + ':'):
                    members = line.split(':')[3].strip().split(',')
                    print("Users in group '{}':".format(group_name))
                    for member in members:
                        print(member)
                    return
        print("Group '{}' not found.".format(group_name))
    except FileNotFoundError:
        print("The file '/etc/group' does not exist.")
    except Exception as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
    list_group_members('team')
