import requests

response = requests.post("http://localhost:8000/color_gen")
Color = response.json()
print(f"{Color=}")
