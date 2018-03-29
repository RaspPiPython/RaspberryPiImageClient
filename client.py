# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 23:03:12 2018

@author: tranl
"""

# client.py  
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname() 
host = '192.168.0.103'   #server's ip address                          

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
tm = s.recv(1024)                                     

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))