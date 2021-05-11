#!/usr/bin/python3

import subprocess

print("content-type: text/html")
print()

cmd1 = "sudo docker rm -f -v $(sudo docker ps -a -q)"
output = subprocess.getoutput(cmd1)
print(output)

cmd2 = "sudo docker network rm -f $(sudo docker network ps -aq)"
output = subprocess.getoutput(cmd2)
print(output)

