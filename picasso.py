import customtkinter
from CTkMessagebox import CTkMessagebox
import random as r
import sys

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("tic-tac-toe")
        self.geometry("600x800")
        self.grid_columnconfigure((0,1), weight=1)  
        self.grid_rowconfigure((0,1) , weight=1)
        self.f1 = customtkinter.CTkFrame(self, width = 1000, height = 1500)
        self.f1.grid(row = 0, column = 0, sticky = "nwse")
        self.canvas = customtkinter.CTkCanvas(self.f1, width = 1000, height = 1000)
        self.canvas.grid(row=0, column=1, columnspan=2, sticky="nsew")
        self.button = customtkinter.CTkButton(self.f1, text="Create a Picasso", fg_color="blue", height = 50)
        self.button.grid(row=1, column=1, sticky="nsew")
        self.buttonexit = customtkinter.CTkButton(self.f1, text="exit", height = 50)
        self.buttonexit.grid(row=1, column=2, sticky="nsew")
      
      
      
      
        self.logic = Logic(self.canvas, self.button, self.buttonexit)      
        
      

class Logic:
    def __init__(self, canvas, button, buttonexit):
        super().__init__()
        self.canvas = canvas
        self.button = button
        self.buttonexit = buttonexit
        self.buttonexit.configure(command = sys.exit)
        self.button.configure(command = self.buttonclick)
     
        
    def buttonclick(self):
        self.canvas.delete("all")
        self.canvas.create_line(r.randint(1,950), r.randint(1,950), r.randint(1,950), r.randint(1,950))
        self.canvas.create_line(r.randint(1,950), r.randint(1,950), r.randint(1,950), r.randint(1,950), r.randint(1,950), r.randint(1,950), r.randint(1,950), r.randint(1,950))
        self.canvas.create_oval(r.randint(1,950), r.randint(1,950), r.randint(1,950), r.randint(1,950), fill="red")
        self.canvas.create_oval(r.randint(1,950), r.randint(1,950), r.randint(1,950), r.randint(1,950), fill="blue")
        

app = GUI()
app.mainloop()
