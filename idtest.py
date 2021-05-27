import socket
import binascii
planes =[]
soc = socket.create_connection(('127.0.0.1',30002))
while(1):
    data = soc.recv(2000)
    a,b = (data.split(b';'))
    star,encoded = a.split(b'*')
    binny= bin(int(encoded,16))
    
    #if(binny[0:7] == '0b10001' and binny[7:10] == '101'):
    binar= (str(bin(int(encoded[8:8+14],16))[2:]).zfill(56))
    if( (binar[0:5] == '00100')):
        print(len(binar)) 
        #print(type(encoded[2:]))
        
        
        a = binar[8:]
        st = ''
        for z in range(len(a),0,-6):
            #print(a[z-6:z])
            st = chr(int(a[z-6:z],2)+64)+st
            #print(st)
        planes.append(st[0:3])
        
        for i in set(planes):
            print(i)
    #print(bytearray.fromhex(str(encoded)))
