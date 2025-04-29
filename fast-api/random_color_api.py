from fastapi import FastAPI
import random as r

my_app = FastAPI()


@my_app.post("/color_gen")
async def color_gen():
    color = {
            "R": r.randint(0,255),
            "G": r.randint(0,255),
            "B": r.randint(0,255)
            }
    return color
    