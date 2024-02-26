import requests
import json
#from config import config as cfg

filename = "repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://github.com/AudeAllen/WSAA-coursework/tree/main/labs/'

# this token is no longer valid, becuase it has been pushed to GitHub
# GitHub detects it and invalidates it automatically for security
apikey='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'


response = requests.get(url, auth = ('token', apikey),verify = False)

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)