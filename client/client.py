from file_service_client import *
from encrypt import *
from decrypt import *

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))

command = input("what command would you like to execute : ")
enc = input("Chose kind of encryption \n (0 for plain text) \n (1 for transpose) \n (2 for substitute) : ")

msg = send_msg(command, enc)
s.send(msg.encode())

while True:
    data = s.recv(1024)
    data = data.decode()
    msg = receive_msg(data)
    if not data:
        break

    print(msg)

print('Successfully get the file')
s.close()
print('connection closed')