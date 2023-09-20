from paramiko.client import SSHClient, RejectPolicy 
import json, re

# should add a configure.txt for users to specify settings 
SSH_HOST = 'ip.addy.num.bers'
SSH_PORT = 22 # ssh port service is running on  
SSH_USER = 'username' 

CMD = 'termux-sms-list '

# set this as default if none is specified
HOST-KEY-DIRECTORY = '~/.ssh/known_hosts' # usually ~/.ssh/known_hosts 
# main purpose use Python's Parmiko to ssh into Termux and command phone via Termux's API (Microphone, camera, sms, etc)

# we will use scp to grab a file from the remote server (Android-Termux) in this case!
##      scp user@serverhostname:path/to/file path/to/dest

client = SSHClient()
###### SECURITY ISSUE   #######
# what to do when there is an unknown hostname... 
# usually this will be new servers 
#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#   using AutoAddPolicy or WarningPolicy
###########################################################

#HOSTKEY POLICY = REJECT UNKNOWN HOSTKEYS
#client.set_missing_host_key_policy(RejectPolicy())
client.set_missing_host_key_policy(RejectPolicy)
client.load_system_host_keys(filename=HOST-KEY-DIRECTORY)
client.connect(SSH_HOST, SSH_PORT)
stdin, stdout, stderr = client.exec_command(CMD)

parsed_output = json.load(stdout)
print('\nJson format')
#keywords = ('code','facebook','gmail','etc')
keywords = ('facebook')
#jsonData = [''][0][]

for i in parsed_output:
    message = i['body'].lower()
    print(message)
    if 'facebook' in message:
        print(message)
        fb_code = re.findall(r'[0-9]+', message)
        print(fb_code[0])
        
    elif 'google' in message:
        print(message)
        gm_code = re.findall(r'[0-9]+', message)
        print(gm_code)

    elif 'tech bit' in message:
        print(message)
        tb_code  = re.findall(r'[0-9]+', message)
        print(tb_code[0])# need this so that it wont scan the alphanumeric code maybe condition to check if the string is hybrid letters and numbers!!!


client.close()
