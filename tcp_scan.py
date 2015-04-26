#!/usr/bin/python



# To use:
# ./tcp_scan 192.168.1. 10 22
# or:
# python tcp_scan 127.0.0. 50 80


# This was writen to help me find my machines on my home network. 
# To use inter the base address of the ip you want to scan.
# Then enter the range for example 10 will give a range of 0-9
# Finaly inter the port you want to connect to  


# import libs
import socket
import sys

# defined most of my variables saved target host for last
base_address = sys.argv[1]
host_address = range(int(sys.argv[2]))
target_port = int(sys.argv[3])
ip_range = []


# this function creats the list of ip addresses in the range specified
def _ip_list():
    for i in host_address:
        ip_range.append(base_address+str(i))
      
_ip_list()


# this function trys to make a scoket connection
def _client_socket():
    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #print ("Attempting Connection")
        client.connect((target_host,target_port))
        client.send("GET")
        response = client.recv(4096)
        print ("")
        print ("==============================================")
        print ("Connected to %s:%d" % (target_host,target_port))
        print (response)
        print ("==============================================")
        client.close()
        

    except:
        #print "Connection Failed!"
        pass

# this is where we take the ip addresses and run each one through
# the socket function trying to make a connection      
for i in ip_range:
    target_host = str(i)
    _client_socket()
exit(0)
