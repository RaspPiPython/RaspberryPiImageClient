# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 23:07:23 2018

@author: tranl
"""

# Client written with Object Oriented method
import socket
import cv2
import pickle
import time

class PiImageClient:
    def __init__(self):
        self.s = None
        
    def connectClient(self, serverIP, serverPort):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((serverIP, serverPort))
        
    def closeClient(self):
        self.s.close()
        
    def receiveOneImage(self):
        imageData = b''
        lenData = self.s.recv(8)
        length = pickle.loads(lenData)
        print('Data length is:', length)
        while len(imageData) < length:
            toRead = length-len(imageData)
            imageData += self.s.recv(4096 if toRead>4096 else toRead)
            if len(imageData)%200000 <= 4096:
                print('Received: {} of {}'.format(len(imageData), length))
        return imageData
    
def main():
    ImageClient = PiImageClient()
    ImageClient.connectClient('192.168.0.103', 50009)
    timeStart = time.time()
    imageData = ImageClient.receiveOneImage()
    image = pickle.loads(imageData)
    ImageClient.closeClient()
    
    elapsedTime = time.time() - timeStart
    print('Total elapsed time is: ', elapsedTime)
    cv2.imshow('Picture from server', image)
    cv2.waitKey(0)  
    
    
    
    
if __name__ == '__main__': main()