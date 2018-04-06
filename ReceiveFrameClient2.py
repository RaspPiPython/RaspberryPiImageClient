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

HOST = '192.168.0.101'
PORT = 50009
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('<INFO> Waiting for incoming packages')

i = int(0)
while i<5:
    i+=1
    imageData = b''
    sizeData = s.recv(8)
    lenData = s.recv(8)
    size = pickle.loads(sizeData)
    length = pickle.loads(lenData)
    print('Data size is:', size)
    print('Data length is:', length)
    print('Raw data:', sizeData,'---', lenData)
    
    imageDataLen = len(imageData)
    while imageDataLen < length:
        toRead = length-imageDataLen
        imageData += s.recv(4096 if toRead>4096 else toRead)
        imageDataLen = len(imageData)
        if imageDataLen%100000 <= 4096:
            print('Received:', imageDataLen)
    
    if imageDataLen == length:
        print('Frame {} successfully received: {} bytes in total'.format(i, imageDataLen))
    else:
        print('Failed to receive frame {}, only {} out of {} bytes of the frame is received'.format(i, imageDataLen, length))

    image=pickle.loads(imageData)
    cv2.imshow('Picture from server', image)
    cv2.waitKey(1)
cv2.waitKey(0)

s.close()