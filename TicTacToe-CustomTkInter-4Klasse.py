import customtkinter
from CTkMessagebox import CTkMessagebox

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("tic-tac-toe")
        self.geometry("320x420")
        self.grid_columnconfigure(0, weight=1)  
        self.grid_rowconfigure((0, 1), weight=1)  
        self.buttonlist = []
        self.f1 = customtkinter.CTkFrame(self) #create the main frame
        self.label = customtkinter.CTkLabel(self,text = "Tic-Tac-Toe", fg_color="blue", width = 300, height = 100, corner_radius = 5, font = ("calibri", 42))
        self.label.grid(row = 0, column = 0, padx = 2.5, pady = 2.5)
        self.f1.grid(row = 1, column = 0, sticky = "nwse")
        self.f1.grid_rowconfigure((0, 1, 2), weight=1)  # Board rows expand
        self.f1.grid_columnconfigure((0, 1, 2), weight=1)  # Board columns expand
        self.board()
        self.player1 = "green"
        self.player2 = "red"
        self.player = 0
    
    def board(self):
        for row in range(3):
            for col in range(3):
                button = customtkinter.CTkButton(self.f1, text="", command=lambda row=row, col=col: self.buttonclicked(row, col,), fg_color="blue", width = 100, height = 100)
                button.grid(row = row, column = col, padx = 2.5, pady = 2.5)
                self.buttonlist.append(button)
                
    def reset(self):
        for btn in self.buttonlist:
            btn.configure(fg_color="blue",state = customtkinter.NORMAL)

    def buttonclicked(self, row, col):
        print(f"row {row} col {col} button has been clicked")
        pressed_button = self.buttonlist[row * 3 + col]

        if pressed_button.cget("fg_color") == "blue":  # Ensure the button is not already clicked
            current_player_color = self.player1 if self.player % 2 == 0 else self.player2
            pressed_button.configure(fg_color=current_player_color, state = customtkinter.DISABLED)
            self.player += 1
            self.check_winner()
        
    def check_winner(self):
        board = [btn.cget("fg_color") for btn in self.buttonlist]

        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        if "blue" not in board:
            CTkMessagebox(title="Draw", message=f"Its a draw!")
            self.reset()
            self.player = 0
            return "Draw"
    
        for win in wins:
            if board[win[0]] == board[win[1]] == board[win[2]] and board[win[0]] != "blue":
                winner = board[win[0]]
                CTkMessagebox(title="Game Over", message=f"{winner} wins!")
                self.reset()
                self.player = 0
                return "Win"
                
        return None

app = App()
app.mainloop()