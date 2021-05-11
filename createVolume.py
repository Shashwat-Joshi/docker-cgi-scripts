#!/usr/bin/python3

import cgi

import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
volumeName = mydata.getvalue("x")

cmd = "sudo docker volume create {}".format(volumeName)

output = subprocess.getoutput(cmd)
print(output)

