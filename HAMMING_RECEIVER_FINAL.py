# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:56:07 2020

@author: 18x42
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:05:10 2020

@author: 18x42
"""

import socket
import math

udp_ip_address = "127.0.0.1"
udp_port_no = 5005

clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msgToClient = 'Received'
bytesToSend = str.encode(msgToClient)

clientSock.sendto(bytesToSend,(udp_ip_address, udp_port_no))

message = clientSock.recvfrom(1024)

bitstr = message[0].decode('ascii')

bitstr = [int(i) for i in bitstr]

print("\nReceived message : ",bitstr)

total_bits = len(bitstr)
no_data_bits = math.ceil(math.log2(total_bits))
no_parity_bits = total_bits - no_data_bits

#Detecting error
i = 0
k = 0
count = []
count.append(0)
while i < no_parity_bits:
    k = (2**i)-1
    sum = 0
    while k < len(bitstr):
        for j in range(2**i):
            if k >= total_bits:
                break
            sum += int(bitstr[k])
            k += 1
        k += (i+1)
    if sum % 2 != 0:
        count.append(count[-1]+(2**i))
    i += 1
    
if count[-1]-1 != -1:
    print("\nPosition Inverted : ",count[-1])


#Correction of the received message
bitpos = 0
bitpos = count[-1]-1
if bitpos != 0 and bitpos != -1:
    if bitstr[bitpos] == 0:
        bitstr[bitpos] = 1
    else:
        bitstr[bitpos] = 0

    print("\nCorrected Message : ",bitstr)