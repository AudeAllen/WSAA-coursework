# as rough and ready module for accessing CSO data that is in the pxstat format
# Work needs to be done to this to allow it to read data sets of N dimensions
# Author: Andrew Beatty

from ast import Pass
import requests
import json

urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset):
    with open("assignments/assignment-outputs/cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset),indent=4), file=fp)

def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url,verify = False)
    return response.json()



if __name__ == "__main__":
  
    getAllAsFile("FIQ02")



