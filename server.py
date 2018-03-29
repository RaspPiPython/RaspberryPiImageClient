# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 23:03:12 2018

@author: tranl
"""

# server.py 
import socket                                         
import time
import cv2

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname()                           

port = 9999                                           

# bind to the port
#serversocket.bind((host, port))    
serversocket.bind(('', port))                              

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
    
    key=cv2.waitKey(1) & 0xFF
    print(key)
    print(ord('q'))
    if key==ord('q'):
        break