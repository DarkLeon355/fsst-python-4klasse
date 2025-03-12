import socket
import pickle
from tictactoe import TicTacToe
import os

HOST = '127.0.0.1' 
PORT = 20001

turn = 0

while True:
    try:
        name = str(input("Please type in your name: "))
        break
    except:
        continue

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        break
    except:
        print("No connection to server")

s.sendall(pickle.dumps(name))
opponent_name = pickle.loads(s.recv(1024))  # Receive opponent's name
print(f"You're playing against {opponent_name}, good luck and have fun!")

while True:
    # Receive updated game state or winner from the server
    print("Waiting for server...")
    obj_pickle = s.recv(1024)
    if not obj_pickle:  # Handle disconnection or empty data
        print("\nThe game has ended! (Either a Draw or you were disconnected from the server)")
        print(obj.board[0])
        print(obj.board[1])
        print(obj.board[2])
        break
    obj = pickle.loads(obj_pickle)  # Update the game state with the received data
    try:
        if obj.winner == 'O' or obj.winner == 'X':  # If there's a winner, send it to the server and break
            print("\nThe game has ended!")
            print(obj.board[0])
            print(obj.board[1])
            print(obj.board[2])
            print(f"{obj.winner} is the winner!")
            s.sendall(pickle.dumps(obj))
            print("Restart server and client to play another round!")
            os._exit(0)
        else:
            obj.input()
        s.sendall(pickle.dumps(obj))
    except:
        print("Something went wrong, please reset the server and client.")
        continue