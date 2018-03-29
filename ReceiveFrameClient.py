# client2.py  
import socket, pickle, cv2

#HOST = '192.168.0.103'
#PORT = 50007
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((HOST, PORT))
#arr = ([1,2,3,4,5,6],[1,2,3,4,5,6])
#data_string = pickle.dumps(arr)
#s.send(data_string)

#data = s.recv(4096)
#data_arr = pickle.loads(data)
#s.close()
#print ('Received', repr(data_arr))

HOST = '192.168.0.103'
PORT = 50009
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
imageData = b''
sizeData = s.recv(8)
lenData = s.recv(8)
size = pickle.loads(sizeData)
length = pickle.loads(lenData)
print('Data size is:', size)
print('Data length is:', length)
print('Raw data:', sizeData,'---', lenData)

while len(imageData) < length:
    toRead = length-len(imageData)
    imageData += s.recv(4096 if toRead>4096 else toRead)
    if len(imageData)%100000 <= 4096:
        print('Received:', len(imageData))
    
print('Length of data received:', len(imageData))

image=pickle.loads(imageData)
cv2.imshow('Picture from server', image)
cv2.waitKey(0)

s.close()