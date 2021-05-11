#!/usr/bin/python3


import subprocess

print("content-type: text/html")
print()


cmd = "sudo docker network ls --format 'table{{.ID}}\t{{.Name}}\t{{.Driver}}:{{.Scope}}'" 

output = subprocess.getoutput(cmd)
print(output)

