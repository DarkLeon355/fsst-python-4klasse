import socket
import pickle
from tictactoe import TicTacToe
import threading

class Server:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 20001
        self.active_clients = []
        self.is_active = True
        self.game = TicTacToe()
        self.player = 0
        self.lock = threading.Lock()  # Thread safety
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(5)
        print("Server is waiting for connections...")
        self.manage_connections()

    def send_game(self):
        """Send the current game state to all players."""
        with self.lock:
            for client in self.active_clients:
                try:
                    client.sendall(pickle.dumps(self.game))
                except Exception as e:
                    print(f"Error sending game state: {e}")
                    self.active_clients.remove(client)

    def client_handler(self, connection, address):
        """Handle an individual client connection."""
        print(f"Connection established with {address}")

        with self.lock:
            self.active_clients.append(connection)

        try:
            while True:
                self.send_game()
                rply = connection.recv(1024)
                
                if not rply:
                    break  # Client disconnected
                
                data = pickle.loads(rply)
                self.game = data
                print(f"Received move from player {self.player}")

                # Switch turn
                self.player = 1 if self.player == 0 else 0

                # Check if there is a winner
                if self.game.winner:
                    print(f"Game over! Winner: {self.game.winner}")
                    self.send_game()  # Send final game state
                    self.reset_game()  # Reset game for a new session
                    break

        except (ConnectionResetError, ConnectionAbortedError):
            print(f"Lost connection with {address}")

        finally:
            with self.lock:
                if connection in self.active_clients:
                    self.active_clients.remove(connection)
            connection.close()

    def reset_game(self):
        """Reset the game and wait for new connections."""
        with self.lock:
            self.game = TicTacToe()
            self.player = 0
            print("Game reset. Waiting for new players...")
            self.manage_connections()

    def manage_connections(self):
        """Manage incoming client connections."""
        try:
            while len(self.active_clients) < 2:
                conn, addr = self.sock.accept()
                print(f"Player connected: {addr}")
                threading.Thread(target=self.client_handler, args=(conn, addr), daemon=True).start()
        except Exception as e:
            print(f"Error accepting connections: {e}")

if __name__ == '__main__':
    server = Server()
