# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO,
# and stores it into a file called "cso.json".
# Author: Audrey Allen

from ast import Pass
import requests
import json


# The below piece of code splits the url into two parts
urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset):
    with open("assignments/assignment-outputs/cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset),indent=4), file=fp)

def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url,verify = False) # Set verify to false as having issues running due to security on my pc
    return response.json()


# The below piece of code calls the function above 

if __name__ == "__main__":
  
    getAllAsFile("FIQ02") # This is the name of the dataset 



