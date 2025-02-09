import socket
import pickle
from tictactoe import TicTacToe

def handle_client(conn, addr, game, player_turn, player1, player2):
    addr_str = f"{addr[0]}:{addr[1]}"
    print(f"Player connected: {addr}")

    # Wait until both players are connected
    while not (player1[0] and player2[0]):
        pass  # Do nothing, just wait

    print("Both players connected! Game starting...")

    try:
        while True:
            if player_turn[0] == addr_str:
                # Send the game object to the client
                conn.sendall(pickle.dumps(game))

                # Receive updated game object from client
                try:
                    data = conn.recv(4096)
                    if not data:
                        print(f"Player {addr} disconnected.")
                        break
                except Exception as e:
                    print(f"Error receiving data: {e}")
                    break

                # Deserialize the received game object
                received_game = pickle.loads(data)

                if isinstance(received_game, str) and received_game in ['X', 'O']:
                    print(f"Winner: {received_game}")
                    break

                # Update game state
                game.board = received_game.board
                game.player = received_game.player

                # Switch turns
                player_turn[0] = player2[0] if addr_str == player1[0] else player1[0]

        print(f"Closing connection with {addr}")
        conn.close()

    finally:
        # Handle player disconnection
        if addr_str == player1[0]:
            player1[0] = ""
        elif addr_str == player2[0]:
            player2[0] = ""

def server():
    HOST = '127.0.0.1'
    PORT = 20001
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)

    print("Server is waiting for players...")

    game = TicTacToe()  # Full game object
    player_turn = [""]
    player1 = [""]
    player2 = [""]

    while True:
        conn, addr = s.accept()
        addr_str = f"{addr[0]}:{addr[1]}"

        if player1[0] == "":
            player1[0] = addr_str
            print(f"Player 1 joined: {addr}")
        elif player2[0] == "":
            player2[0] = addr_str
            print(f"Player 2 joined: {addr}")
        else:
            print(f"Rejected connection from {addr} (Game full)")
            conn.close()
            continue

        # If both players are connected, start handling clients
        if player1[0] and player2[0]:
            player_turn[0] = player1[0]  # Set turn to Player 1
            print("Both players are connected. Starting game!")

            # Start handling clients in parallel
            handle_client(conn, addr, game, player_turn, player1, player2)

if __name__ == '__main__':
    server()
