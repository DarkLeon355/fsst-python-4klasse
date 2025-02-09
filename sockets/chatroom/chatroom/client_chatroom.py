'''
einfacher echo client
erste Uebung fuer Sockets in Python

Mai 2021
Markus
'''

import socket
import threading
import random

class EchoClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.on = True
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.color_lst = [ "\x1b[32m", "\x1b[33m", "\x1b[34m", "\x1b[35m", "\x1b[36m", "\x1b[90m", "\x1b[91m", "\x1b[92m", "\x1b[93m", "\x1b[94m", "\x1b[95m", "\x1b[96m"]
        self.lst = []

    def inp(self):
        self.s.sendall(input("\x1b[37m").encode())
        while self.on:
            print("\x1b[37m", end="")
            data = input("\x1b[37m")
            self.s.sendall(data.encode())
            if data == "end":
                self.on = False
                break

    def run(self):
        print("welcome to the echo server, please type what you want and 'end' to quit")
        x = threading.Thread(target=self.inp)
        x.start()
        while self.on:
            try:
                data = self.s.recv(1024)
                if not data:
                    break
                user, data = data.decode().split(":")
                if user not in self.lst:
                    self.lst.append((user, random.choice(self.color_lst)))
                color = [x[1] for x in self.lst if x[0] == user][0]
                print(color + user + data, end="")
                print("\x1b[37m")
            except ConnectionAbortedError:
                break
        print("Client interrupted and shutting down...")
        print("cleaning up ...")
        self.s.close()

if __name__ == "__main__":
    client = EchoClient('10.10.217.153', 61111)
    client.run()
