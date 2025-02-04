'''
einfacher echo client
erste Uebung fuer Sockets in Python
'''

import socket

HOST = '127.0.0.1' 
PORT = 61111      
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("welcome to the echo server, please type what you want and 'end' to quit")
while True:
    data = input()
    if (data == "end"):
        break
    s.sendall(data.encode())
    data = s.recv(1024)
    print('Received:', data.decode())

print("cleaning up ...")
s.close()