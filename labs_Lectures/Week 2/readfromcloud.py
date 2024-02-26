import requests
import json
#import certifi
#ssl._create_default_https_context = ssl._create_unverified_context  


url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url,verify=False)
#print (response.json())
data = response.json()
#with open ("bitcoindump.json", "w") as fp:
#    json.dump(data, fp)

bpi = data["bpi"]
#print(bpi)
rate = bpi["EUR"]["rate"]
print(rate) 	