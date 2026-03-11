books = []

def getall():
    return books

def findById(id):
    for book in books:
        if book["id"] == id:
            return book
    return None

def create(book):
    book["id"] = len(books) + 1
    books.append(book)
    return book

def update(id, book):
    existing = findById(id)
    if existing:
        existing.update(book)
        return existing
    return None

def delete(id):
    book = findById(id)
    if book:
        books.remove(book)
        return True
    return False