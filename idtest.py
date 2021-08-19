import socket
import binascii
import csv
import os

planes =[]
soc = socket.create_connection(('127.0.0.1',30002))



with open('table-1.csv', mode ='r') as f:
    reader = csv.reader(f)
    di = {rows[1]:rows[2] for rows in reader}


while(1):
    data = soc.recv(2000)
    try:
        a,b = (data.split(b';'))
    
        star,encoded = a.split(b'*')
        binny= bin(int(encoded,16))
        
        #if(binny[0:7] == '0b10001' and binny[7:10] == '101'):
        binar= (str(bin(int(encoded[8:8+14],16))[2:]).zfill(56))
        if( (binar[0:5] == '00100')):
            print(len(binar)) 
            #print(type(encoded[2:]))
            os.system('cls||clear')

            
            a = binar[8:]
            st = ''
            for z in range(len(a),0,-6):
                #print(a[z-6:z])
                decodedchar = int(a[z-6:z],2)
                if decodedchar<27:
                    st = chr(decodedchar+64)+st
                else:
                    st = chr(decodedchar)+st
                #st = chr(int(a[z-6:z],2)+64)+st
                #print(st)
            print('Latest: ',st)
            planes.append(st[0:3])
            print('Flights thus far:')
            print('_________________')
            for i in sorted(set(planes)):
                try:
                    print(di[i])
                except:
                    print(i)
    except:
        print(data,'failed')
    #print(bytearray.fromhex(str(encoded)))
