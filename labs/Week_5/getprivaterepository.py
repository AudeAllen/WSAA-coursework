import requests
import json
#from config import config as cfg

filename = "labs/Lab_output/repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://github.com/AudeAllen/WSAA-coursework/tree/main/assignments'

# this token is no longer valid, becuase it has been pushed to GitHub
# GitHub detects it and invalidates it automatically for security
apikey='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'
# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

#apikey = cfg["githubkey"]


response = requests.get(url, auth = ('token', apikey),verify = False)

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)