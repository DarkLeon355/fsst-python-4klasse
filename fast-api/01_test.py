from fastapi import FastAPI
import random

my_app = FastAPI()

#the shopping list
shopping_list = []

@my_app.get("/shopping")
async def get_shopping_list():
    return shopping_list

@my_app.post("/shopping")
async def add_item(item):
    shopping_list.append(item)
    return "OK"
    
@my_app.post("/random")
async def randint():
    return(random.randint(1,1000))