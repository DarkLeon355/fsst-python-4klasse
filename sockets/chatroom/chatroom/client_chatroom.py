import socket
import threading

class ChatClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.active = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server_ip, self.server_port))

    def transmit(self):
        username = input("Enter your username: ").strip()
        self.sock.sendall(username.encode())

        while self.active:
            try:
                msg = input()
                self.sock.sendall(msg.encode())
                if msg.lower() == "end":
                    self.active = False
                    break
            except (ConnectionResetError, ConnectionAbortedError):
                break

    def listen(self):
        while self.active:
            try:
                data = self.sock.recv(1024)
                if not data:
                    break
                print(data.decode().strip())
            except (ConnectionResetError, ConnectionAbortedError):
                break

        print("Disconnected from the server.")
        self.sock.close()

    def start(self):
        print("Connected to the chat. Type 'end' to exit.")

        send_thread = threading.Thread(target=self.transmit)
        receive_thread = threading.Thread(target=self.listen, daemon=True)

        send_thread.start()
        receive_thread.start()

        send_thread.join()

if __name__ == "__main__":
    client = ChatClient('127.0.0.1', 61111)
    client.start()

