import socket
import threading
import keyboard

class ChatServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.active_clients = []
        self.is_active = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock.listen()
        print(f"Server running on {self.ip}:{self.port}")
    
    def send_message(self, msg, sender=None):
        for client in self.active_clients:
            if client != sender:
                try:
                    client.sendall(msg)
                except:
                    self.active_clients.remove(client)
    
    def client_handler(self, connection, address):
        print(f"Connection established with {address}")
        try:
            username = connection.recv(1024).decode().strip()
            join_msg = f"\x1b[31mSERVER: {username} has joined the chat\n".encode()
            self.send_message(join_msg, connection)
            self.active_clients.append(connection)

            while True:
                msg = connection.recv(1024)
                if not msg:
                    break

                formatted_msg = f"{username}: {msg.decode()}\n".encode()
                print(formatted_msg.decode().strip())
                self.send_message(formatted_msg, connection)

                if msg.decode().strip().lower() == "end":
                    break
        
        except (ConnectionResetError, ConnectionAbortedError):
            print(f"Lost connection with {address}")
        finally:
            self.active_clients.remove(connection)
            connection.close()
            exit_msg = f"\x1b[31mSERVER: {username} has left the chat\n".encode()
            self.send_message(exit_msg)
            print(f"{address} disconnected.")
    
    def manage_connections(self):
        while self.is_active:
            try:
                conn, addr = self.sock.accept()
                threading.Thread(target=self.client_handler, args=(conn, addr), daemon=True).start()
            except:
                break
    
    def start(self):
        threading.Thread(target=self.manage_connections, daemon=True).start()
        try:
            while True:
                if keyboard.is_pressed('esc'):
                    print("Server shutting down...")
                    self.is_active = False
                    self.sock.close()
                    break
        except KeyboardInterrupt:
            print("Server interrupted. Closing...")
            self.sock.close()

if __name__ == "__main__":
    chat_server = ChatServer('127.0.0.1', 61111)
    chat_server.start()
