#!/usr/bin/python3

import cgi

import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
imagename = mydata.getvalue("x")

cmd = "sudo docker rm -f {}".format(imagename)

output = subprocess.getoutput(cmd)
print(output)

