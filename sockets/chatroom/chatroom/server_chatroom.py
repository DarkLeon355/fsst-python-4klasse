'''
Echo server mit multi threading - ist in der Lage
mit mehr als einem Client gleichzeitig zu sprechen

zweite Uebung fuer Sockets in Python

Mai 2021
Markus
'''

import socket
import threading
import keyboard

class EchoServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.lst = []
        self.start_again = True
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen()

    def echo(self, conn, addr):
        print('Connected by', addr)
        name = conn.recv(1024)
        for i in self.lst:
            i.sendall(f"\x1b[31mSERVER: {name.decode()} has joined the chat\n".encode())
        self.lst.append(conn)
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                data = name + b": " + data
                print(repr(data))
                for c in self.lst:
                    if c != conn:
                        c.sendall(data)
                if data.decode().endswith("end"):
                    self.lst.remove(conn)
                    for c in self.lst:                       
                        c.sendall(f"\x1b[31mSERVER: {name.decode()} has left the chat\n".encode())
                    break
            except ConnectionAbortedError:
                break
            except OSError:
                break
            except:
                self.lst.remove(conn)
                self.start_again = False
                break
        
        conn.close()

    def accept_connections(self):
        while self.start_again:
            conn, addr = self.s.accept()
            echo_thread = threading.Thread(target=self.echo, args=(conn, addr))
            echo_thread.start()

    def run(self):
        accept_thread = threading.Thread(target=self.accept_connections)
        accept_thread.start()
        try:
            while True:
                if keyboard.is_pressed('q'):
                    print("Shutting down server...")
                    self.s.close()
                    break
        except KeyboardInterrupt:
            print("Server interrupted and shutting down...")
            self.s.close()

if __name__ == "__main__":
    server = EchoServer('10.10.217.153', 61111)
    server.run()

