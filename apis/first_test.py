import requests
import json

url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
params = {"s": "Moscow Mule"}
response = requests.get(url, params=params).json()
#print(response)
ingredients = f" You need {response['drinks'][0]['strIngredient1']}"
insturctions = response['drinks'][0]['strInstructions']
print(f"{ingredients} \n {insturctions}")

