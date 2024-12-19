import customtkinter
import random as r
from PIL import Image, ImageTk
import requests
import json
from urllib.request import urlretrieve
from pprint import PrettyPrinter
from datetime import date
import time

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Picasso")
        self.geometry("680x700")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        # Main frame
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)  # Button column
        self.main_frame.grid_columnconfigure(1, weight=1)  # Exit button column
        self.main_frame.grid_columnconfigure(2, weight=1)  # NASA button column
        self.main_frame.grid_rowconfigure(0, weight=10)  # Canvas row
        self.main_frame.grid_rowconfigure(1, weight=1)  # Button row

        # Canvas
        self.canvas = customtkinter.CTkCanvas(self.main_frame, width=680, height=600)
        self.canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")

        # Drawing logic instanz aufrufen
        self.drawer = Draw(self.canvas)
        self.nasa = GetNasa(self.canvas, self.main_frame)
        
        # knöpfe
        self.button_draw = customtkinter.CTkButton(
            self.main_frame, text="Create a Picasso", command=self.draw)
        self.button_draw.grid(row=1, column=0, sticky="ew")

        self.button_exit = customtkinter.CTkButton(self.main_frame, text="Exit", command=self.quit)
        self.button_exit.grid(row=1, column=1, sticky="ew")
        
        self.button_nasa = customtkinter.CTkButton(self.main_frame, text="Nasa Picture of the Day", command=self.nasa.get_pic)
        self.button_nasa.grid(row=1, column=2, sticky="ew")
        
    def draw(self):
        self.nasa.destroy_pic_text()
        self.drawer.draw_shapes()


class Draw:
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas

    def draw_shapes(self):
        self.canvas.delete("all")
        for _ in range(5):  # Adjust the number of shapes as needed
            self.draw_random_line()
            self.draw_random_oval()

    def draw_random_line(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        self.canvas.create_line(
            r.randint(0, canvas_width), r.randint(0, canvas_height),
            r.randint(0, canvas_width), r.randint(0, canvas_height),
            fill=f"#{r.randint(0, 255):02x}{r.randint(0, 255):02x}{r.randint(0, 255):02x}", width=5
        )

    def draw_random_oval(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        self.canvas.create_oval(
            r.randint(0, canvas_width), r.randint(0, canvas_height),
            r.randint(0, canvas_width), r.randint(0, canvas_height),
            fill=f"#{r.randint(0, 255):02x}{r.randint(0, 255):02x}{r.randint(0, 255):02x}"
        )


class GetNasa:
    def __init__(self, canvas, main_frame):
        super().__init__()
        self.canvas = canvas
        self.main_frame = main_frame
    
    def pic_to_canvas(self):
        # Load a PNG image
        image = Image.open("nasa_apod_hd.jpg")  # Replace with your PNG file path
        image = image.resize((680, 600), Image.Resampling.LANCZOS)  # Resize as needed
        self.photo_image = ImageTk.PhotoImage(image)

        # Display the image on the canvas
        self.canvas.delete("all")
        self.canvas.create_image((self.canvas.winfo_width()/2), (self.canvas.winfo_height()/2), image=self.photo_image, anchor="center")  # Adjust position as needed
        self.label = customtkinter.CTkLabel(self.main_frame,text = self.response.get('explanation', 'No explanation available') , fg_color="grey", width = 300, height = 100, corner_radius = 5, font = ("calibri", 16), wraplength=650)
        self.label.grid(row=2, column=0, columnspan=3, sticky="nsew")
    
    
    def destroy_pic_text(self):
        try:
            self.canvas.delete("all")
            self.label.destroy()
        except:
            x = 1
    
    
    def get_pic(self):
        pp = PrettyPrinter()
        url = "https://api.nasa.gov/planetary/apod"
        self.date = date.today()
        params = {'api_key': "UGGDC8d1871ZWnJ7nlJSV6GNoOB9HwnKUownAiwe",'date':self.date,'hd':'True'}
        self.response = requests.get(url,params=params).json()
        pp.pprint(self.response)
        urlretrieve(self.response['hdurl'], "nasa_apod_hd.jpg")
        pp.pprint(self.response)
        self.pic_to_canvas()
        


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
