# server.py
from encrypt import *
from decrypt import *
from file_service_server import *
import os
import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:

   conn, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   data = conn.recv(1024)
   print('Server received', data.decode())
   data = data.decode()
   enc,cmd,client_inp = receive_msg(data)

   print(enc)
   print(cmd)
   print(client_inp)

   msg = send_msg(enc,cmd,client_inp)
   conn.send(msg.encode())
  
   print('Done sending')
   conn.close()