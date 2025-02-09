'''
einfacher echo client
erste Uebung fuer Sockets in Python
'''

import socket
import testclass
import pickle

HOST = '127.0.0.1' 
PORT = 61111      
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

o = testclass.myclass("hello",10)
o_pickle = pickle.dumps(o)
s.sendall(o_pickle)

s.close()
