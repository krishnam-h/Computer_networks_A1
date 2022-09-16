# Computer_networks_A1
Krishnam Hasija 19110184
Computer Networks Assignment 1

The repository consists of two folders a client and a server.

Client directory contains the following files : 
  
  - client.py
  
  - encrypt.py
  
  - decrypt.py
  
  - file_service_client.py
  
  - mytext_client.txt
  
  
Server directory contains the following files : 

  - server.py
  
  - encrypt.py
  
  - decrypt.py
  
  - file_service_server.py
  
  - server_data   (folder)
  
    - mytext_server.txt


In order to run the code, first navigate to the server directory and run the file server.py by running
```console
python server.py
```
This will start the server and it will accept responses from the client, it will continue running and client can give multiple commands.

Open another terminal tab and navigate to the client directory. Run the file client.py by running
```console
python client.py
```
Enter your command, either 'cwd', 'ls', 'cd dir_path', 'dwd file_name_or_path' or 'upd file_name_or_path' (e.g. upd mytext_client.txt)
You will be asked to enter the mode of encryption that you want for your message
  enter 0 (for plain text), 1 (for transpose) or 2 (for substitute)

After this your command will run and you will receive a response from the server.

In order to run another command you must run the client file (python client.py) again and enter your command.
