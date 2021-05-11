#!/usr/bin/python3

import cgi

import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
networkName = mydata.getvalue("x")

cmd = "sudo docker network create -d bridge {}".format(networkName)

output = subprocess.getoutput(cmd)
print(output)

