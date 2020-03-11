# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:37:11 2020

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

clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msgToClient = 'Received'
bytesToSend = str.encode(msgToClient)

clientSock.sendto(bytesToSend,(udp_ip_address, udp_port_no))

message = clientSock.recvfrom(1024)

receivedMsg = message[0].decode('ascii')

receivedMsg = receivedMsg.split(';')

msg = receivedMsg[0]
div = receivedMsg[1]
code = receivedMsg[2]

print('Received Message : ',msg)
print('Divisor : ',div)
print('Code:', code)
print('Success:', crc(msg, div, code) == '000')
