# Author: Audrey Allen

# Write a python program called currentweather.py
# that will print out the current temperature on the console (and only the temperature)

# print out the current wind direction (10m) as well

import requests
import json
import warnings
warnings.filterwarnings("ignore")

## The code below is to extract the current temperature in the below location

url = "https://api.open-meteo.com/v1/forecast?latitude=52.71&longitude=-8.5003&current=temperature_2m"
response = requests.get(url,verify = False) ## This was put into the code as due to security settings on my pc it was

data = response.json()

current_units = data["current"]

temperature_2m = current_units["temperature_2m"]

print (f' Your current temperature is: {temperature_2m}') 




## The code below is to extract the current wind speed in the below location

url = "https://api.open-meteo.com/v1/forecast?latitude=52.71&longitude=-8.5003&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
response = requests.get(url,verify = False) ## This was put into the code as due to security settings on my pc it was

data = response.json()

current_units = data["current"]

wind_speed_10m = current_units["wind_speed_10m"]


# Print out result
print (f' Your current wind speed is: {wind_speed_10m}') 
 	

