import socket
import pickle
from tictactoe import TicTacToe
import os
import time
import threading

HOST = '127.0.0.1' 
PORT = 20001

class client:
    def getname(self):
        while True:
            try:
                self.name = str(input("Please type in your name: "))
                break
            except:
                continue
        self.connect()
    
    def connect(self):
        self.turn = 0
        print(f"fettsack2222222")
        while True:
            print(f"fettsack333333")
            try:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((HOST, PORT))
                print("Da device is a connected succesfullay")
                break
            except:
                print("No connection to server")
                time.sleep(1)
                
        self.s.sendall(pickle.dumps(self.name))
        opponent_name = pickle.loads(self.s.recv(1024))  # Receive opponent's name
        print(f"You're playing against {opponent_name}, good luck and have fun!")
        self.gamehandler()

    def gamehandler(self):
        try:
            while True:
                # Receive updated game state or winner from the server
                print("Waiting for server...")
                obj_pickle = self.s.recv(1024)
                if not obj_pickle:  # Handle disconnection or empty data
                    print("\nThe game has ended! (Either a Draw or you were disconnected from the server)")
                    print(obj.board[0])
                    print(obj.board[1])
                    print(obj.board[2])
                    cont=str(input("Enter q to quit or anything else to continue: "))
                                    
                    if cont != "q":
                            self.s.sendall(pickle.dumps(cont))                      
                            time.sleep(5)
                            print(f"fettsack")
                            if self.s:
                                self.obj = TicTacToe() #this resets it clienstide (I know illegal)
                                self.s.recv(1024)   #Signal to reset finally please work
                                return
                            else:
                                return

                    else:
                        os._exit(0)

                obj = pickle.loads(obj_pickle)  # Update the game state with the received data
                try:
                    if obj.winner == 'O' or obj.winner == 'X':  # If there's a winner, send it to the server and break
                        print("\nThe game has ended!")
                        print(obj.board[0])
                        print(obj.board[1])
                        print(obj.board[2])
                        print(f"{obj.winner} is the winner!")
                        self.s.sendall(pickle.dumps(obj))
                        cont=str(input("Enter q to quit or anything else to continue: "))
                                    
                        if cont != "q":
                            self.s.sendall(pickle.dumps(cont))                      
                            time.sleep(5)
                            print(f"fettsack")
                            if self.s:
                                self.obj = TicTacToe() #this resets it clienstide (I know illegal)
                                self.s.recv(1024)   #Signal to reset finally please work
                                return
                            else:
                                return

                        else:
                            os._exit(0)
                    else:
                        obj.input()
                    self.s.sendall(pickle.dumps(obj))
                except:
                    print("Something went wrong, please reset the server and client.")
                    continue
        except:
            return

c=client()
client.getname(c)
while True:
    client.connect(c)
