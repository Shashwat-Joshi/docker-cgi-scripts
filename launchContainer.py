#!/usr/bin/python3

import cgi

import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
osname = mydata.getvalue("x")
imagename = mydata.getvalue("y")

cmd = "sudo docker run -dit --name {} {}".format(osname,imagename)

output = subprocess.getoutput(cmd)
print(output)

