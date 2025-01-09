import customtkinter

class InputFields(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1), weight=1) 
        self.grid_rowconfigure((1, 2), weight=1)
        
        self.titleframe = customtkinter.CTkFrame(self,fg_color="gray",height=40)
        self.titleframe.grid(row=0, column=0, padx=10, pady=10, sticky="nesw", columnspan=2)

        self.title = customtkinter.CTkLabel(self.titleframe,text="Please input a language then press the button")
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)

        self.language = customtkinter.CTkEntry(self,fg_color="Black",text_color="white")
        self.language.grid(row=1, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)
        self.vocab = customtkinter.CTkTextbox(self,fg_color="Black",text_color="white",state="disabled",activate_scrollbars=False,height=1)
        self.vocab.grid(row=2, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)
        self.playerinput = customtkinter.CTkEntry(self,fg_color="Black",text_color="white")
        self.playerinput.grid(row=2, column=1, padx=10, pady=10, sticky="nesw", columnspan=1)

        self.languagebutton = customtkinter.CTkButton(self,fg_color="Green",text_color="Green",text="",width=100,height=100,command=self.getinputs,corner_radius=0)
        self.languagebutton.grid(row=1, column=1, padx=10, pady=10, sticky="nesw", columnspan=1)

        self.languageselected = False #To help return the correct value first

    def getinputs(self):
        self.language = self.selectedlanugage=self.language.get()
        self.playerinput = self.filledplayerinput=self.playerinput.get()
        print(self.selectedlanugage)
        print(self.filledplayerinput)
        if self.languageselected == True:
            return (self.playerinput)
        else:                               #Returns the language and the next time the button is pressed the translated word
            if self.language == None:
                self.languageselected = False
            else:
                self.languageselected = True
            return (self.language)


    def vocabcheck(self,vocab,playervocab):

        playervocab = self.playerinput
        if vocab == playervocab:
            ""

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Vocab Trainer")
        self.geometry("400x300")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        self.inputs = InputFields(master=self)
        self.inputs.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

app = GUI()
app.mainloop()