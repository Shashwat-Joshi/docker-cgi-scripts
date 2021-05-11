#!/usr/bin/python3


import subprocess

print("content-type: text/html")
print()


cmd = "sudo docker ps --format 'table{{.Names}}'" 

output = subprocess.getoutput(cmd)
print(output)

