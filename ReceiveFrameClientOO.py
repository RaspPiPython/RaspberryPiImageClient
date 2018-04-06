# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 01:39:55 2018

@author: tranl
"""

import socket
import cv2
import pickle
import time

class PiImageClient:
    def __init__(self):
        self.s = None
        self.counter = 0
        
    def connectClient(self, serverIP, serverPort):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((serverIP, serverPort))
        
    def closeClient(self):
        self.s.close()
        
    def receiveOneImage(self):
        imageData = b''
        lenData = self.s.recv(8)
        length = pickle.loads(lenData) # should be 921764 for 640x480 images
        print('Data length is:', length)
        while len(imageData) < length:
            toRead = length-len(imageData)
            imageData += self.s.recv(4096 if toRead>4096 else toRead)
            #if len(imageData)%200000 <= 4096:
            #    print('Received: {} of {}'.format(len(imageData), length))
        return imageData
    
    def receiveFrame(self):        
        imageData = b''
        lenData = self.s.recv(8)
        length = pickle.loads(lenData)
        print('Data length is:', length)
        #length = 921764 # for 640x480 images
        while len(imageData) < length:
            toRead = length-len(imageData)
            imageData += self.s.recv(4096 if toRead>4096 else toRead)
            if len(imageData)%200000 <= 4096:
                print('Received: {} of {}'.format(len(imageData), length))
        self.counter += 1
        if len(imageData) == length: 
            print('Successfully received frame {}'.format(self.counter))                
        return imageData
    
def main():
    ImageClient = PiImageClient()
    ImageClient.connectClient('192.168.0.101', 50009)
    print('<INFO> Connection established, preparing to receive frames...')
    timeStart = time.time()
    
    while(1):
        imageData = ImageClient.receiveFrame()
        image = pickle.loads(imageData)
        #print(image[0])
        cv2.imshow('Frame', image)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
    
    #imageData = ImageClient.receiveOneImage()
    #image = pickle.loads(imageData)
    ImageClient.closeClient()
    
    elapsedTime = time.time() - timeStart
    print('Total elapsed time is: ', elapsedTime)
    #cv2.imshow('Picture from server', image)
    cv2.waitKey(0)  
    
    
    
    
if __name__ == '__main__': main()