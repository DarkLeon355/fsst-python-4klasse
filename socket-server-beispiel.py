'''
einfacher echo server
erste Uebung fuer Sockets in Python
'''

import socket

HOST = '127.0.0.1' 
PORT = 61111      

#IPv4 TCP Socket erzeugen und auf Clients warten (lauschen)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
#bis zu 5 clients werden im backlog gehalten!
s.listen(5)


while True:

    conn, addr = s.accept()
    print('Connected by', addr)

    while True:
        #.recv mit verschiedenen Byte-Laengen ausprobieren!
        data = conn.recv(1024)
        if not data:
           break
        #man kann auch .decode() verwenden, statt repr
        print('Received from client', repr(data))
        #.sendall ist komfortabler als .send(byte-laenge)
        conn.sendall(data)
    conn.close()

