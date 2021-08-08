import paramiko
import time
import getpass
# creating an ssh client object
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)

# the line at below only works in cmd!!
password = getpass.getpass('enter the password:')
router = {'hostname': '10.1.1.3', 'port': '22', 'username':'admin', 'password':password}
print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)  # using **kwargs

# checking if the connection is active
print(ssh_client.get_transport().is_active())

# sending commands
# ...

shell = ssh_client.invoke_shell()
shell.send('show version\n')
time.sleep(1)

output =shell.recv(1000)
output = output.decode('utf-8')
print(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()