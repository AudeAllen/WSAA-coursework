import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getallbooks():
      response = requests.get(url)  
      return response.json()

def getBookById(id):
      geturl = url + "/" + str(id)
      response = requests.get(geturl)
      return response.json()
  
def CreateBook(book):
      book= {
            'Author':"Test1",
            'Title':"Test Title1",
            'Price':150
      }

     # First way to create book
     #response = requests.post(url, json=(book))
     #return response.json() 
      
      # More complex way to create book

      headers = {"Content-type": "application/json"}
      response = requests.post(url, data = json.dumps(book), headers = headers)
      return response.json()

     

def UpdateBook(id, bookdiff):
      updateurl = url + "/" + str(id)
      response = requests.put(updateurl, json=bookdiff)
      return response.json()
     

def DeleteBook(id):
      deleteurl = url + "/" + str(id)
      response = requests.delete(deleteurl)
      return response.json()


if __name__=="__main__":
      book= {
            'Author':"Test1",
            'Title':"Test Title1",
            'Price':150
      }

      bookdiff= {
            'Author':"Audrey A",
            'Title':"Test Title1",
            'Price':150
      }
     #print(CreateBook(book))
     # print(UpdateBook(523, bookdiff))
      print (DeleteBook(523))
