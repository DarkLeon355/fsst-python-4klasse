import socket
import pickle
import threading
from tictactoe import TicTacToe

HOST = '127.0.0.1' 
PORT = 20001

class Server:
    def __init__(self):
        self.game = TicTacToe()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen(2)
        print("Server started, waiting for players...")

        self.players = []
        self.names = []
        self.lock = threading.Lock()
        self.current_turn = 0  # Player 0 starts

        # Accept connections from two players
        for i in range(2):
            conn, addr = self.server.accept()
            self.players.append(conn)
            name = pickle.loads(conn.recv(1024)).decode('utf-8')  # Receive player's name
            self.names.append(name)
            print(f"Player {i+1} ({name}) connected from {addr}")

        # Start threads for both players
        for i in range(2):
            thread = threading.Thread(target=self.handle_client, args=(i,))
            thread.start()

def handle_client(self, player_id):
    conn = self.players[player_id]

    while True:
        try:
            with self.lock:
                # Wait until it's this player's turn
                if player_id != self.current_turn:
                    conn.sendall(pickle.dumps("WAIT"))  # Notify player to wait
                    ack = conn.recv(1024)  # Wait for acknowledgment
                    continue  

                # Send game state to the current player
                conn.sendall(pickle.dumps(self.game))

                # Receive move update
                data = conn.recv(1024)

                game = pickle.loads(data)  # Expecting a (row, col) tuple
                
                # **Manually update board since make_move() does not exist**
                row, col = move
                if self.game.board[row][col] == '':  # Check if cell is empty
                    self.game.board[row][col] = 'X' if player_id == 0 else 'O'
                else:
                    conn.sendall(pickle.dumps("INVALID_MOVE"))  # Notify invalid move
                    continue

                # Check for a winner
                winner = self.game.checkwin()
                if winner:
                    print(f"We have a winner: {winner}")
                    for player in self.players:
                        player.sendall(pickle.dumps(winner))
                    return

                # Switch turn
                self.current_turn = 1 - self.current_turn  

                # Send updated game state to the other player
                other_player = self.players[self.current_turn]
                other_player.sendall(pickle.dumps(self.game))

        except Exception as e:
            print(f"Error: {e}")
            break

    conn.close()


# Start the server
if __name__ == "__main__":
    Server()
