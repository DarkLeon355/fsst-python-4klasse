class TicTacToe:
    def __init__(self):
        self.rows, self.cols = 3, 3
        self.board = [['' for _ in range(self.cols)] for _ in range(self.rows)]
        self.player = 0
        self.winner = None
        
    def input(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        while True:
            self.p_row = int(input("\nPlease type in Row:"))
            if self.p_row > 3 or self.p_row < 1:
                continue
            self.p_col = int(input("Please type in Column:"))
            if self.p_col > 3 or self.p_col < 1:
                continue
 
            self.p_row = self.p_row - 1
            self.p_col = self.p_col - 1
            
            if self.board[self.p_col][self.p_row] != '':
                print("Already used!")
                continue
            else:
                break
        
        # Update board with player's move
        if self.player == 0:
            self.board[self.p_col][self.p_row] = 'X'
            self.player = 1
        elif self.player == 1:
            self.board[self.p_col][self.p_row] = 'O'
            self.player = 0
        
        # Check for winner
        self.checkwin()
        
    def checkwin(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                self.winner = row[0]
        
        # Check columns
        for col in range(self.cols):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                self.winner = self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            self.winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            self.winner = self.board[0][2]
        
        return None  # No winner yet
        
