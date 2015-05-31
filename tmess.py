#!/usr/bin/python

import socket
import tty
#import sign   this is a lib I use to sign my work

print  "\n \n"
#print sign.yaps()   this printed a logo
print "\n \n "
host = raw_input("Inter Target Address: \n>>> "
port = int(raw_input("Inter Port: \n>>> ")) 
message = raw_input("Inter Message: \n>>> ")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
client.send("%s" % message)
recv = client.recv(1024)

print recv

