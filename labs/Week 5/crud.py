from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary data storage
books = [
    {"id": 1, "title": "Book One", "author": "Author A", "price": 10}
]

# GET ALL
@app.route('/books', methods=['GET'])
def getall():
    return jsonify(books)

# GET BY ID
@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return {"error": "Not found"}, 404

# CREATE
@app.route('/books', methods=['POST'])
def create():
    newbook = request.json
    newbook["id"] = len(books) + 1
    books.append(newbook)
    return jsonify(newbook)

# UPDATE
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    for book in books:
        if book["id"] == id:
            book.update(request.json)
            return jsonify(book)
    return {"error": "Not found"}, 404

# DELETE
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"deleted": True}
    return {"error": "Not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)