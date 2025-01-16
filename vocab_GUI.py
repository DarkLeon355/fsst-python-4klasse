import customtkinter
import vocab_trainer_ai_req as ai


class InputFields(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("C:/Users\Mario/OneDrive - HTL Anichstrasse/Desktop/Fsst collectione/FSST/4.Klasse/Fettsack/fsst-python-4klasse/themes/breeze.json")
        self.grid_columnconfigure((0, 1), weight=1) 
        self.grid_rowconfigure((1, 2), weight=1)
        
        self.titleframe = customtkinter.CTkFrame(self,height=40)
        self.titleframe.grid(row=0, column=0, padx=10, pady=10, sticky="nesw", columnspan=2)

        self.title = customtkinter.CTkLabel(self.titleframe,text="Please input a language then press the button:")
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)

        self.language = customtkinter.CTkEntry(self)
        self.language.grid(row=1, column=0, padx=10, pady=10, sticky="nesw", columnspan=1)
        self.vocab = customtkinter.CTkTextbox(self,state="disabled",activate_scrollbars=False,height=1)
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
        

    def getinputs(self):
        self.selectedlanguage=self.language.get()
        self.checkplayerinput()
        print(self.selectedlanguage)
        print(self.filledplayerinput)
        if self.selectedlanguage == None:
            self.languagebutton.configure(self,text="Input required",command=self.getinputs,corner_radius=0)
        else:
            self.languagebutton.configure(self,text="",command=self.getinputs,corner_radius=0)
            self.initialize()
            self.vocabcheck()
        
    def checkplayerinput(self,event=None):
        self.filledplayerinput =self.playerinput.get()
        return(self.filledplayerinput)
        
    def vocabcheck(self):
        for index, (key, value) in enumerate(self.dictionary.items()):

            self.currentvocab = self.dictionary(key,value)
            self.filledplayerinput = self.checkplayerinput()

            if self.currentvocab == self.filledplayerinput:
                self.playerinput.configure(self,fg_color="Green",text_color="white")
            else:
                self.playerinput.configure(self,fg_color="Red",text_color="white")
        print(self.filledplayerinput)
        print(self.currentvocab)
        self.after(500, self.vocabcheck)

    def initialize(self):
        self.createdictionary()

    def createdictionary(self):
        self.dictionary = ai.AIReq(self.selectedlanguage).dic
        for index, (key, value) in enumerate(self.dictionary.items()):
            print(f"Index: {index}, Key: {key}, Value: {value}")


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