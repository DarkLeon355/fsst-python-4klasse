import requests
import json

params = {"name":"lelek","type":"Powerplant"}
url = "https://10.5.101.0:7272/powergrid/Register"

lelek_name = requests.post(url, json=params, verify = False)
print(lelek_name)
i = lelek_name.text

while True:
    power = requests.post("https://10.5.101.0:7272/powergrid/ChangeEnergy", {f"{i}"}, verify = False)
    print("produced energy")

    


#while True():
   # if requests.post("https://10.5.101.0:7272/powergrid/ChangeEnergy", ").status_code == 200:
        #response = requests.get(url, lololol).json()