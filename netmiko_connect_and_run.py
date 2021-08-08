# from netmiko import Netmiko
# connection = Netmiko(host='10.1.1.10', port='22', username='u1', password='cisco', device_type='cisco_ios')

from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '10.1.1.3',
       'username': 'admin',
       'password': 'admin',
       'port': 22,             # optional, default 22
       'secret': 'admin',      # this is the enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

# sending a command and getting the output

output = connection.send_command('sh ip int brief')
#print(output)

if not connection.check_enable_mode():
       connection.enable()
print(connection.find_prompt())
if not connection.check_config_mode():
       connection.config_mode()
print(connection.find_prompt())

connection.send_command('do sh run')
print(connection.find_prompt())

connection.exit_config_mode()
connection.exit_enable_mode()

# closing the connection
print('Closing connection')
connection.disconnect()