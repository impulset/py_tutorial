import subprocess

ip_address = '192.168.9.1'
ping_command = subprocess.run(['ping', '-c 2', '-a', f'{ip_address}'], capture_output=True, text=True) 

print(ping_command.stdout) #stdout allows access command output
print(ping_command.returncode) #if command completed succesfully returns 0

print(subprocess.run(['rm', '-r', 'test']).returncode)