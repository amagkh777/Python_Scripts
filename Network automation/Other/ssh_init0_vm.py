import subprocess
import os

data_server={'server':['192.168.1.5','root' ,'1q2w!Q@W',22],
             'asterisk':['192.168.1.7','root', '1q2w!Q@W',22],
             'eve':['192.168.1.3','root' ,'eve',22],

             }

for keys in data_server.keys():
    host, user, secret, port = data_server[keys]
    respone =os.popen(f'ping  {host}').read()
    if "TTL" in respone:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=secret, port=port)
        stdin, stdout, stderr = client.exec_command('init 0')
        data = stdout.read() + stderr.read()
        client.close()
    else:
        continue
