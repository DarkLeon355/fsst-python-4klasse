import socket
import pickle
from tictactoe import TicTacToe
import threading
import time
import os

class Server:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 20001
        self.active_clients = []
        self.client_names = []
        self.is_active = True
        self.game = TicTacToe()
        self.player = 0
        self.turn = 0
        self.activethreads = 0
        self.lock = threading.Lock()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(2)
        self.threadlist=[]
        print("Server is waiting for a connection...")
        self.manage_connections()

    def send_game(self):
        with self.lock:
            if len(self.active_clients) < 2:
                print("Not enough players to send game state.")
                return  # Prevent out-of-range errors
            
            for self.client in self.active_clients:
                if self.client != self.active_clients[self.player]:
                    try:
                        self.client.sendall(pickle.dumps(self.game))
                        self.turn = self.turn + 1
                    except Exception as e:
                        print(f"Error sending game state: {e}")
                        self.active_clients.remove(self.client)

    def client_handler(self, connection, address):
        print(f"Connection established with {address}")
        try:
            name = pickle.loads(connection.recv(1024))  # Receive player's name
            print("fuckwar123123d")
            with self.lock:
                self.active_clients.append(connection)
                self.client_names.append(name)
            print("fuckward")
            if len(self.client_names) == 2:
                # Send opponent's name to each client
                self.active_clients[0].sendall(pickle.dumps(self.client_names[1]))
                self.active_clients[1].sendall(pickle.dumps(self.client_names[0]))

            while True:
                self.send_game()
                rply = connection.recv(1024)
                if not rply:
                    break
                
                data = pickle.loads(rply)
                self.game = data
                print(f"Sent and received game from player {self.player}")
                self.player = 1 if self.player == 0 else 0
                
                if self.turn == 9:
                    self.send_game()
                    print(f"Game ended in a draw. Waiting for player decision")
                    print("Fatardbefore")
                    rply = connection.recv(1024)        #Waiting for player to Reset or leave
                    print("Fatardafter")
                    if rply != "q":
                        print("FatardDONE")
                        return 0
                    
                    else:
                        time.sleep(2)
                        os._exit(0)

                if self.game.winner in ['O', 'X']:
                    self.send_game()
                    print(f"Game won by {self.game.winner}. Waiting for player decision")
                    print("Fatardbefore")
                    rply = connection.recv(1024)        #Waiting for player to Reset or leave
                    print("Fatardafter")
                    if rply != "q":
                        print("FatardDONE")
                        return 0
                        
                        
                    else:
                        time.sleep(2)
                        os._exit(0)
                    
        except (ConnectionResetError, ConnectionAbortedError):
            print(f"Lost connection with {address}")
        finally:
            with self.lock:
                if connection in self.active_clients:
                    self.active_clients.remove(connection)
                if name in self.client_names:
                    self.client_names.remove(name)
                print("stupidshit")
                connection.close()

    def manage_connections(self):
        try:
            while len(self.active_clients) < 2:
                try:
                    conn, addr = self.sock.accept()
                    print("fuckward connectionhandler")
                    self.threadlist.append(threading.Thread(target=self.client_handler, args=(conn, addr), daemon=True).start())

                except Exception as e:
                    print(f"Error accepting connections: {e}")
                    break
        except Exception as e:
            print(f"Server error: {e}")

        if self.threadlist[1] != None:
            self.threadlist[0].join()
            try:
                self.threadlist[1].join()
            except:
                pass

            for client in self.active_clients[:]:   #loop trough
                try:
                    print(f"Reset {client}")
                    client.sendall(pickle.dumps("resetthatshit"))
                except Exception as e:
                    print(f"Failed to send reset signal: {e}")

            time.sleep(1)
            self.game = TicTacToe()     #reset shit but doesnt
            self.player = 0
            self.turn = 0
            self.sock.close                 #If both clients arent disconnected before this happens we're fucked cuz Im too lazy or not enough cognitive function to get around that :3 wawwaawwawawawa
            self.__init__()                 #A lot of this stuff is useless probably but its too late already ngl lets just hope this works 

if __name__ == '__main__':
    while True:
        server = Server()           #I bin amal ehrlich es is jetza 23:00 und der code is so mieß scheiße i kann nimma idk warum des board nit resetted aber i bin einfach fertig i mach des jetza scho 4 stunden oder so straight
        Server.__init__()   