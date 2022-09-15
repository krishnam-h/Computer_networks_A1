from encrypt import *
from decrypt import *
import os

 
def listdirs(rootdir, list_of_dirs):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            list_of_dirs.append(d)
            listdirs(d, list_of_dirs)


def receive_msg(msg):
    
    enc = msg.split()[-1]
    client_inp = msg[:-2]
    cmd = client_inp.split()[0].strip()
    
    if(len(client_inp.split()) > 1):
        client_inp = client_inp.split()[1:]
        client_inp = " ".join(client_inp)

    if(enc == '0'):
        return enc,cmd,client_inp
    
    elif(enc == '1'):
        return enc,decrypt_transpose(cmd), decrypt_transpose(client_inp)

    elif(enc == '2'):
        return enc,decrypt_substitute(cmd), decrypt_substitute(client_inp)

    return 


def send_msg(enc,cmd,msg):

    if(cmd == "cwd"): 
        my_cwd = os.getcwd()

        if(enc == '0'):
            return my_cwd + ' 0'
        
        elif(enc == '1'):
            return encrypt_transpose(my_cwd) + ' 1'
        
        elif(enc == '2'):
            return encrypt_substitute(my_cwd) + ' 2'

    elif(cmd == "ls"): 
        send_ms = ""
        my_ls = os.listdir()
        for file_name in my_ls:
            send_ms = send_ms + '\n' + file_name
        
        if(enc == '0'):
            return send_ms + ' 0'
        
        elif(enc == '1'):
            return encrypt_transpose(send_ms) + ' 1'

        elif(enc == '2'):
            return encrypt_substitute(send_ms) + ' 2'

    elif(cmd == "cd"): 
        my_cwd = os.getcwd()
        list_of_dirs = []
        listdirs(my_cwd, list_of_dirs)

        new_dir = os.path.join(my_cwd,msg)
        if new_dir in list_of_dirs:
            os.chdir(new_dir)

            if(enc == '0'):
                return "you are now in " + new_dir + ' 0'
            
            elif(enc == '1'):
                return encrypt_transpose("you are now in " + new_dir) + ' 1'

            elif(enc == '2'):
                return encrypt_substitute("you are now in " + new_dir) + ' 2'

        else:
            if(enc == '0'):
                return "Directory " + new_dir + " does not exist" + ' 0'

            elif(enc == '1'):
                return encrypt_transpose("Directory " + new_dir + " does not exist") + ' 1'

            elif(enc == '2'):
                return encrypt_substitute("Directory " + new_dir + " does not exist") + ' 2'


    elif(cmd == "dwd"): 

        my_cwd = os.getcwd()

        if(os.path.isfile(msg)):
            final_file_dir = msg
            f = open(final_file_dir,'r')
            txt = ""
            l = f.read()
            txt = txt + l
            while (l):
                l = f.read()
                txt = txt + l

            f.close()

            if(enc == '0'):
                return '**write_file** ' + txt + ' 0'
            
            elif(enc == '1'):
                return  "**write_file** " + encrypt_transpose(txt) + ' 1'

            elif(enc == '2'):
                return "**write_file** " + encrypt_substitute(txt) + ' 2'

        elif(os.path.isfile(os.path.join(my_cwd,msg))):   
            final_file_dir = os.path.join(my_cwd,msg)
            f = open(final_file_dir,'r')
            txt = ""
            l = f.read()
            txt = txt + l
            while (l):
                l = f.read()
                txt = txt + l

            f.close()
            if(enc == '0'):
                return  "**write_file** " + txt + ' 0'
            
            elif(enc == '1'):
                return  "**write_file** " + encrypt_transpose(txt) + ' 1'

            elif(enc == '2'):
                return  "**write_file** " + encrypt_substitute(txt) + ' 2'


        else:
            if(enc == '0'):
                return "File does not exist" + ' 0'

            elif(enc == '1'):
                return encrypt_transpose("File does not exist") + ' 1'

            elif(enc == '2'):
                return encrypt_substitute("File does not exist") + ' 2'

        return

    elif(cmd == "upd"): 

        fp = open('uploaded_file.txt','w')
        data = msg.split()[2:]
        data = " ".join(data)
        
        fp.write(data)
        fp.close()
        
        if(enc == '0'):
            return "File uploaded" + " 0"

        elif(enc == '1'):
            return encrypt_transpose("File uploaded") + " 1"
        
        elif(enc == '2'):
            return encrypt_substitute("File uploaded") + " 2"


    else: 
        return -1


