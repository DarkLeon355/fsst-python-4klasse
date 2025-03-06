import socket
import pickle
from tictactoe import TicTacToe


HOST = '127.0.0.1' 
PORT = 20001


while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        break
    except:
        print("No connection to server")



while True:
    # Receive updated game state or winner from the server
    print("Waiting for server...")
    obj_pickle = s.recv(1024)
    if not obj_pickle:  # Handle disconnection or empty data
        print("Connection closed by the server.")
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
            
            response = input("Want to play another game (yes/no): ").strip().lower()
            if response == "no":
                break
            elif response == "yes":
                s.close()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
            else:
                print("Wrong input, ending game")
                break

            
        else:
            obj.input()
        s.sendall(pickle.dumps(obj))

    except:
        print("Something went wrong, please reset the server and client.")
        continue