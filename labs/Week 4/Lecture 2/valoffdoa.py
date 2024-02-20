import requests
import json
import urllib.parse
url = "https://opendata.tailte.ie/api/Property/GetProperties"


ParametersasDict = {
      
"Download":"False",
"Format":"json",
"CategorySelected":"OFFICE",
"LocalAuthority":"WICKLOW COUNTY COUNCIL",
"Fields":"LocalAuthority,Category,Level,NavTotal,RateableValuation,CarPark,PropertyNumber,ITM,Use,FloorUse,Address,Eircode,PublicationDate"

}

def getAllValuations():
      response = requests.get(url,verify=False)  
      parameters = urllib.parse.urlencode(ParametersasDict)
      #print (parameters)

      fullurl = url + "?" + parameters
      response = requests.get(fullurl,verify=False)

      return response.json()


if __name__ == "__main__":
      with open("valoff.json", "wt") as fp:
            print(json.dumps(getAllValuations()), file = fp) 