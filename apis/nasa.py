import requests
import json
from urllib.request import urlretrieve
from datetime import date
from PIL import Image

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

while True:
    try:
        datum = input("Input date YYYY-MM-DD: ")
        params = {'earth_date': datum, 'api_key': ""}
        if requests.get(url, params=params).status_code == 200:
            response = requests.get(url, params=params).json()
            break
    except:
        print("Wrong date")
        continue

if response["photos"]:
    image_url = response["photos"][0]["img_src"]
    print(f"Image URL: {image_url}")  # Print the image URL for debugging
    urlretrieve(image_url, "C:/code/GitHub/fsst-python/apis/rover_pic.jpg")
    print("Image fetched successfull.")
    while True:
        try:
            i = str(input("Want to display the image? yes/no: "))
            break
        except:
            continue

    if i == "yes":
        image = Image.open('rover_pic.jpg')
        image.show()
        print(response["photos"][0]["rover"])
        print(response["photos"][0]["camera"])
else:
    print("No photos available for the given date.")



    
