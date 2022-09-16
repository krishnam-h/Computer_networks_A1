# server.py
from encrypt import *
from decrypt import *
from file_service_server import *
import socket                   

port = 60000                    
s = socket.socket()             
host = socket.gethostname()     
s.bind((host, port))           
s.listen(5)                     

print('Server listening....')

while True:

   conn, addr = s.accept()     
   print('Got connection from', addr)
   data = conn.recv(1024)
   print('Server received', data.decode())
   data = data.decode()
   enc,cmd,client_inp = receive_msg(data)

   print(enc)
   print(cmd)
   print(client_inp)

   msg = send_msg(enc,cmd,client_inp)
   print(f"Server response: {msg}")
   print(f"Server response in hex: ",msg.encode().hex())
   conn.send(msg.encode())
  
   print('Done sending')
   conn.close()