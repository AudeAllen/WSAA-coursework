import requests
import json
#from config import config as cfg

filename = "repos-putrepo.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://github.com/AudeAllen/WSAA-coursework/tree/main/labs_Lectures'

# this token is no longer valid, becuase it has been pushed to GitHub
# GitHub detects it and invalidates it automatically for security
apikey='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'


file_name = "labs/Lab_output/example.txt"
file = open(file_name, "rb")

print(f"{file_name} was read with rb and\nI get this type of data {type(file)}")

response = requests.put(url, auth = ('token', apikey),verify = False, data=file)

print (response.status_code)
#print (response.json())

#if response.status_code == 201:
#    print("File attached successfully")
#else:
#    print("Failed to attach file. Response status code:", response.status_code)