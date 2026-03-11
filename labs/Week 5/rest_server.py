import bookdao

from flask import Flask, request, jsonify
import bookdao

app = Flask(__name__)

# GET ALL
@app.route('/books', methods=['GET'])
def getall():
    return jsonify(bookdao.getall())

# GET BY ID
@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    book = bookdao.findById(id)
    if book:
        return jsonify(book)
    return {"error": "Not found"}, 404

# CREATE
@app.route('/books', methods=['POST'])
def create():
    newbook = request.json
    return jsonify(bookdao.create(newbook))

# UPDATE
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    updated = bookdao.update(id, request.json)
    if updated:
        return jsonify(updated)
    return {"error": "Not found"}, 404

# DELETE
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    success = bookdao.delete(id)
    if success:
        return {"deleted": True}
    return {"error": "Not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)