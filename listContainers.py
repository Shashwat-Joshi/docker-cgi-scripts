#!/usr/bin/python3


import subprocess

print("content-type: text/html")
print()


cmd = "sudo docker ps --format 'table{{.Names}}\t{{.ID}}\t{{.Image}}'" 

output = subprocess.getoutput(cmd)
print(output)

