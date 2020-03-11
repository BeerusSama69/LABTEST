# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:51:55 2020

@author: 18x42
"""

import socket
import math

udp_ip_address = "127.0.0.1"
udp_port_no = 5005

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind((udp_ip_address,udp_port_no))

data = input('Enter the Data : ')
no_data_bits = len(data)

no_parity_bits = math.ceil(math.log2(no_data_bits))+1

total_bits = no_data_bits + no_parity_bits

bitstr = [0 for x in range(total_bits)]
for i in range(no_parity_bits):
    bitstr[pow(2,i)-1] = 'P'

k = 0
for j in range(total_bits):
    if bitstr[j] == 0:
        bitstr[j] = data[k]
        k += 1
    
i = 0
k = 0
while i < no_parity_bits:
    k = (2**i) - 1
    sum = 0
    while k < len(bitstr):
        for j in range(2**i):
            if k >= total_bits:
                break
            if bitstr[k] == 'P':
                k += 1
                continue
            else:
                sum += int(bitstr[k])
                k += 1
        k += (i+1)
    if sum % 2 == 0:
        bitstr[bitstr.index('P')] = '0'
    else:
        bitstr[bitstr.index('P')] = '1'
    i += 1

print('Encoded Message : ',bitstr)

p = int(input('Enter the Bit Position inverted : '))

if bitstr[p-1] == '0':
    bitstr[p-1] = '1'
else:
    bitstr[p-1] = '0'
    
strbitstr = ''.join([str(i) for i in bitstr])
bytesToSend = str.encode(strbitstr)

while True:
    bytesAddressPair = serverSock.recvfrom(1024)
    address = bytesAddressPair[1]
    
    serverSock.sendto(bytesToSend,address)
    
 