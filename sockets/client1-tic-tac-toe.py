import socket
import pickle
from tictactoe import TicTacToe


HOST = '127.0.0.1' 
PORT = 61111      
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))



while True:
    # Receive updated game state or winner from the server
    obj_pickle = s.recv(1024)
    if not obj_pickle:  # Handle disconnection or empty data
        print("Connection closed by the server.")
        break
    obj = pickle.loads(obj_pickle)  # Update the game state with the received data
    
    winner = obj.input()
    if winner:  # If there's a winner, send it to the server and break
        s.sendall(pickle.dumps(winner))
        break
    else:
        # Send the updated game state (the TicTacToe object) to the server
        s.sendall(pickle.dumps(obj))
        
