import customtkinter
import vocab_trainer_ai_req as ai
from CTkMessagebox import CTkMessagebox


class InputFields(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.vocablist=[]
        self.keylist=[]

        self.realindex=0

        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("themes/breeze.json")
        self.grid_columnconfigure((0, 1), weight=1) 
        self.grid_rowconfigure((1, 2), weight=1)
        
        self.titleframe = customtkinter.CTkFrame(self,height=40)
        self.titleframe.grid(row=0, column=0, padx=10, pady=10, sticky="nesw", columnspan=2)

        self.title = customtkinter.CTkLabel(self.titleframe,text="Please input a language then press the button:")
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)
      
        self.language = customtkinter.CTkEntry(self)
        self.language.grid(row=1, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)
        self.vocab = customtkinter.CTkTextbox(self,activate_scrollbars=False,height=1)
        self.vocab.grid(row=3, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)
        self.vocablabelframe = customtkinter.CTkFrame(self)
        self.vocablabelframe.grid(row=2, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)
        self.vocablabel = customtkinter.CTkLabel(self.vocablabelframe,text="This is the word to translate:")
        self.vocablabel.grid(row=0, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)
        self.playerinput = customtkinter.CTkEntry(self)
        self.playerinput.grid(row=3, column=1, padx=10, pady=10, sticky="nesw", columnspan=1)
        self.playerinputframe = customtkinter.CTkFrame(self)
        self.playerinputframe.grid(row=2, column=1, padx=10, pady=10, sticky="nesw", columnspan=1)
        self.playerlabel = customtkinter.CTkLabel(self.playerinputframe,text="Your translation:")
        self.playerlabel.grid(row=0, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)

        self.languagebutton = customtkinter.CTkButton(self, text="Submit Language", command = self.getinputs)
        self.languagebutton.grid(row=1, column=1, padx=10, pady=10, sticky="nesw", columnspan=1)
        self.languageselected = False #To help return the correct value first
        
        self.checkbutton = customtkinter.CTkButton(self, text = "Check Input", command = self.checkplayerinput)
        self.checkbutton.grid(row=10, column=1, columnspan=2, padx = 10, pady = 10, sticky = "nswe")
        

    def getinputs(self):
        self.index = 0
        self.selectedlanguage=self.language.get()
        print(self.selectedlanguage)
        if self.selectedlanguage == None:
            self.languagebutton.configure(self,text="Input required",command=self.getinputs,corner_radius=0)
        else:
            self.initialize()
            self.displayvocab()
        
    def checkplayerinput(self):
        self.filledplayerinput = self.playerinput.get()
        if self.filledplayerinput == self.awnsers[self.index]:
            print("True")
            self.checkbutton.configure(fg_color = "green")
            self.index = self.index + 1
        
            self.displayvocab()
        else:
            self.checkbutton.configure(fg_color = "red")
            print("False")
        
        if self.index == 21:
            self.restart()
            
    def restart(self):
        self.deutsch = []
        self.awnsers = []
        CTkMessagebox(title="Restart", message=f"Please type in a new Language")
        
   
    def displayvocab(self):
        print(self.deutsch)
        print(self.awnsers)
        self.vocab.delete("0.0", "end")
        self.vocab.insert("0.0", self.deutsch[self.index])
        


    def initialize(self):
        self.getvocab()

    def getvocab(self):
        self.dictionary = ai.AIReq(self.selectedlanguage).dic
        self.deutsch = (list(self.dictionary.keys()))
        self.awnsers = (list(self.dictionary.values()))
            


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