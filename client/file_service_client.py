from encrypt import *
from decrypt import *
import os

def send_msg(msg, enc):

    cmd = msg.split()[0].strip()
    if(cmd == "dwd"):
        fp = open('downloaded_file.txt','w')

    elif(cmd == "upd"):

        client_inp = msg.split()[1:]
        client_inp = " ".join(client_inp)
        my_cwd  = os.getcwd()

        if(os.path.isfile(client_inp)):
            final_file_dir = client_inp
            f = open(final_file_dir,'r')
            txt = ""
            l = f.read()
            txt = txt + l
            while (l):
                l = f.read()
                txt = txt + l

            f.close()

            if(enc == '0'):
                return msg + ' **upload_file** ' + txt + ' 0'
            
            elif(enc == '1'):
                return  encrypt_transpose(msg) + " **upload_file** " + encrypt_transpose(txt) + ' 1'

            elif(enc == '2'):
                return encrypt_substitute(msg) + " **upload_file** " + encrypt_substitute(txt) + ' 2'


        elif(os.path.isfile(os.path.join(my_cwd,client_inp))):   
            final_file_dir = os.path.join(my_cwd,client_inp)
            f = open(final_file_dir,'r')
            txt = ""
            l = f.read()
            txt = txt + l
            while (l):
                l = f.read()
                txt = txt + l

            f.close()
            if(enc == '0'):
                return msg + ' **upload_file** ' + txt + ' 0'
            
            elif(enc == '1'):
                return  msg + " **upload_file** " + encrypt_transpose(txt) + ' 1'

            elif(enc == '2'):
                return msg + " **upload_file** " + encrypt_substitute(txt) + ' 2'


        else:
            print("File does not exist")
            return

    
    
    if(enc == '0'):
        return msg + ' ' + enc
    
    elif(enc == '1'):
        return encrypt_transpose(msg) + ' ' + enc
    
    elif(enc == '2'):
        return encrypt_substitute(msg) + ' ' + enc


def receive_msg(msg):

    if(msg == ""):
        return None
    
    enc = msg.split()[-1]
    check_dwd = msg.split()[0]
    msg = msg[:-2]
    
    if(check_dwd == "**write_file**"):
        with open("downloaded_file.txt",'w') as f:
            msg = msg.replace("**write_file** ","")
            if(enc == '0'):
                f.write(msg)

            elif(enc == '1'):
                f.write(decrypt_transpose(msg))
            
            elif(enc == '2'):
                f.write(decrypt_substitute(msg))
        
        return "file downloaded"
        
    else:
        if(enc == '0'):
            return msg
        
        elif(enc == '1'):
            return decrypt_transpose(msg)

        elif(enc == '2'):
            return decrypt_substitute(msg)

    

def info():
    return ''' The following commands are supported:
    1. CWD - Retrieve the path of the current working directory for the user
    2. LS - List the files/folders present in the current working directory
    3. CD <dir> - Change the directory to <dir> as specified by the client
    4. DWD <file> - Download the <file> specified by the user on server to client
    5. UPD <file> - Upload the <file> on client to the remote server in CWD'''