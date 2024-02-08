# Author: Audrey Allen

# Write a python program called currentweather.py
# that will print out the current temperature on the console (and only the temperature)

# print out the current wind direction (10m) as well

import requests
import json
import warnings
warnings.filterwarnings("ignore")


url = "https://api.open-meteo.com/v1/forecast?latitude=52.71&longitude=-8.5&current=temperature_2m"
response = requests.get(url,verify = False) ## This was put into the code as due to security settings on my pc it was

data = response.json()

current_units = data["current"]

temperature_2m = current_units["temperature_2m"]
print(temperature_2m) 	



