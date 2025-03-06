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
        self.win = False
        self.game = TicTacToe()
        self.player = 0
        self.lock = threading.Lock()  # Create a lock for thread-safe access
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(5)
        print("Server is waiting for a connection...")
        self.manage_connections()

    def send_game(self):
        with self.lock:
            for client in self.active_clients:
                if client != self.active_clients[self.player]:
                    try:
                        client.sendall(pickle.dumps(self.game))
                    except Exception as e:
                        print(f"Error sending game state: {e}")
                        self.active_clients.remove(client)

    def client_handler(self, connection, address):
        print(f"Connection established with {address}")
        try:
            with self.lock:
                self.active_clients.append(connection)
            while True:
                self.send_game()
                rply = connection.recv(1024)
                if not rply:
                    break
                data = pickle.loads(rply)
                self.game = data
                print(f"Sent and recieved game from {self.player}")
                self.player = 1 if self.player == 0 else 0

        except (ConnectionResetError, ConnectionAbortedError):
            print(f"Lost connection with {address}")
        finally:
            with self.lock:
                self.active_clients.remove(connection)
            connection.close()

    def manage_connections(self):
        try:
            while len(self.active_clients) < 2:
                try:
                    conn, addr = self.sock.accept()
                    threading.Thread(target=self.client_handler, args=(conn, addr), daemon=True).start()
                except Exception as e:
                    print(f"Error accepting connections: {e}")
                    break
        except:
            print("Server is at full capacity")

if __name__ == '__main__':
    server = Server()