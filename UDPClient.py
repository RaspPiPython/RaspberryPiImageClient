# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 00:43:57 2018

@author: tranl
"""

import socket
import sys
import pickle

# Create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

HOST = 'localhost'
clientIP = socket.gethostbyname(socket.gethostname())
serverIP = '192.168.0.101'
PORT = 50009
addr = (serverIP, PORT)
#addr = pickle.dumps(addr)
#msg = '<BEGIN>'
msg = pickle.dumps(clientIP)

s.sendto(msg, addr)
print('Message sent')

while len(data) < 921764:
    
