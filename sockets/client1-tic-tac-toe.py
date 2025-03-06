import socket
import pickle
from tictactoe import TicTacToe

HOST = '127.0.0.1' 
PORT = 20001

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        n = input("Please type in your Name: ")
        s.sendall(pickle.dumps(n.encode('utf-8')))  # Send name as pickled data
        break
    except:
        print("No connection to server")

while True:
    # Receive updated game state or a turn wait signal
    obj_pickle = s.recv(1024)
    if not obj_pickle:  
        print("Connection closed by the server.")
        break

    data = pickle.loads(obj_pickle)

    if data == "WAIT":
        print("Waiting for the other player's move...")
        continue  # Skip this iteration and wait for the next game state

    game = data  # Update the game state with the received data
    game.input()

    s.sendall(pickle.dumps((game)))
