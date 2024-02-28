# Author: Audrey Allen

# Write a program in python that will read a file from a repository. 

# The program should then replace all the instances of the text "Andrew" with your name. 

# The program should then commit those changes and push the file back to the repositoryYou will need authorisation to do this).



# to use this install package
# pip install PyGithub
from github import Github
import requests
from config import config as cfg



apikey = cfg["githubkey"]


# config file is in .gitignore file as I do not want the key uploaded to github

g = Github(apikey,verify = False) # This is the key you get from github - Put this into your config file


# Get repo in Github - AudeAllen/Test
repo = g.get_repo("AudeAllen/Test")
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile,verify = False)
contentOfFile = response.text
print (contentOfFile)


# Adding name AndrewB to text.txt file - This is because it has been ran previously and been replaced

newContents = contentOfFile + " AndrewB AndrewB AndrewB AndrewB AndrewB AndrewB AndrewB AndrewB AndrewB AndrewB AndrewB\n" 
print (newContents)

# Replacing AndrewB with AudeAllen - In text.txt fil
 
string = contentOfFile
new_string = string.replace("AndrewB", "AudeAllen")
print(new_string)
 
# Update file in github with  commit message and updated by prog message
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog - Replace",new_string,fileInfo.sha)
print (gitHubResponse)
