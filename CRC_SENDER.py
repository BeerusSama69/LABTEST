# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:29:15 2020

@author: 18x42
"""

def crc(msg,div,code):
    
    msg = msg + code
    msg = list(msg)
    div = list(div)
    for i in range(len(msg)-len(code)):
        if msg[i] == '1':
            for j in range(len(div)):
                msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)

    return ''.join(msg[-len(code):])

import socket
import math

udp_ip_address = "127.0.0.1"
udp_port_no = 5005

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind((udp_ip_address,udp_port_no))

msg = input('Enter the Message : ')
div = input('Enter the Divisor : ')
check_bit = len(div)-1

codeadditional = ['0' for i in range(check_bit)]
codeadditional = ''.join(codeadditional)

code = crc(msg, div,codeadditional)

print('\n\n')
print('Input Message : ',msg)
print('Input Divisor : ',div)
print('Output code:', code)

n1 = int(input('Any Bit inverted : (1/0) ? '))

if n1 == 1:
    n = int(input('Enter the Bit position inverted : '))
    msg = list(msg)
    print(msg)
    if msg[n-1] == '1':
        msg[n-1] = '0'
    else:
        msg[n-1] = '1'
    
    msg = ''.join(msg)

finalMsg = []

finalMsg.append(msg)
finalMsg.append(div)
finalMsg.append(code)

l=''
for i in finalMsg:
    l+=i
    l+=';'

finalMsg = l
bytesToSend = str.encode(finalMsg)

while True:
    bytesAddressPair = serverSock.recvfrom(1024)
    address = bytesAddressPair[1]
    
    serverSock.sendto(bytesToSend,address)