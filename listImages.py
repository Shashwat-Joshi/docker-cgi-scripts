#!/usr/bin/python3


import subprocess

print("content-type: text/html")
print()


cmd = "sudo docker images --format 'table{{.Repository}}:{{.Tag}}\t{{.Size}}'" 

output = subprocess.getoutput(cmd)
print(output)

