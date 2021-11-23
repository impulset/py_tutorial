import subprocess

ip_address = '192.168.9.1'
ping_command = subprocess.run(['ping', '-c 2', '-a', f'{ip_address}'], capture_output=True, text=True) 

print(ping_command.stdout) #stdout allows access command output
print(ping_command.returncode) #if command completed succesfully returns 0

def create_folder(name):
    print("Creating folder.....")
    result = subprocess.run(['mkdir', f'{name}']).returncode
    if result == 0:
        print(f'{name} was successfully created')

def remove_folder(name):
    result = subprocess.run(['rm', '-r', f'{name}']).returncode
    if result == 0:
        print(f'{name} was successfully removed')

remove_folder("new_test1")

