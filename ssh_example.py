## connect to an ssh server and remotely execute a command

import paramiko

hostname = "192.168.1.15"
port = 22

username = "??"
password = "??"

s = paramiko.SSHClient(hostname, port, username, password)

results = s.exec_command("ls -l")

print results

s.close()


