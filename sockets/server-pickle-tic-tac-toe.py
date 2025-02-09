import socket
import pickle
from tictactoe import TicTacToe

def server():
    HOST = '127.0.0.1' 
    PORT = 61111
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print("Server is waiting for a connection...")

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        game = TicTacToe()
        

        while True:
            
            # Send the game object to the client
            conn.sendall(pickle.dumps(game))
            
            # Receive data from the client
            data = conn.recv(1024)

            if not data:
                break  # If no data is received, the connection is closed
            
            # Deserialize the received data
            game = pickle.loads(data)
            
            if game == 'X' or game == 'O':
                print(game)
                break

        conn.close()  # Close the connection after processing
        print("Connection closed.")
      

server()
