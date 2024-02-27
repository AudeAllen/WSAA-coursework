# to use this install package
# pip install PyGithub
from github import Github
import requests
from config import config as cfg




apikey = cfg["githubkey"]

g = Github(apikey,verify = False)

verify = False
repo = g.get_repo("AudeAllen/Test")
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile,verify = False)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + " more stuff 2 \n"
print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)
