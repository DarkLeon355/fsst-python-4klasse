import requests
from datetime import date
from urllib.request import urlretrieve
import randtime
import time 

def random_time():
        generator = randtime.RandomTimeGenerator("2020-01-01", "2025-01-01")
        print(date.today())
        return generator.random_date()

def get_pics():
        url = "https://api.nasa.gov/planetary/apod"
        for i in range(10):
            date = random_time()
            params = {'api_key': "UGGDC8d1871ZWnJ7nlJSV6GNoOB9HwnKUownAiwe",'date':date,'hd':'True'}
            response = requests.get(url,params=params).json()
            url_pic = response['hdurl']
            pic_name = f"nasa_{i}"
            urlretrieve(url_pic, f"C:/code/GitHub/fsst-python/project_memory/{pic_name}.jpg")
            time.sleep(3)

get_pics()
