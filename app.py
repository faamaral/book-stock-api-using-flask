from flask import Flask, jsonify, request
from random import randint
import json
app = Flask(__name__)

i = randint(0, 1000)
books = [
    {
        "key": 0,
        "identificator": i,
        "title": "Hello world",
        "author": "Nobody",
        "category": ["Education", "Programing", "Computer"],
        "published": 2015
    },
    {
        "key": 1,
        "identificator": i+1,
        "title": "Two buildings",
        "author": "Test",
        "category": ["Education", "Enginner"],
        "published": 2017
    }
]

@app.route("/books/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def book(id):
    if request.method == 'GET':
        try:
            response = books[id]
        except IndexError:
            response = {"status": "ERROR!"}
        return jsonify(response)

    elif request.method == 'PUT':
        data = json.loads(request.data)
        books[id] = data
        return jsonify(data)
    elif request.method == 'DELETE':
        books.pop(id)
        return jsonify({"Status": 200, "MESSAGE":"THIS BOOK HAS BEEN DELETED"})

@app.route("/books/", methods=['POST', 'GET'])
def list_books():
    if request.method == 'POST':
        data = json.loads(request.data)
        pos = len(books)
        data["key"] = pos
        books.append(data)
        return jsonify({"STATUS": "sucess"})
    elif request.method == 'GET':
        return jsonify(books)


@app.route("/calc", methods=['POST', 'GET'])
def calc():
    if request.method == 'POST':
        soma = json.loads(request.data)
        total = sum(soma['values'])
        print(soma)
    elif request.method == 'GET':
        total = 3+7
    return jsonify({'soma': total})

if __name__ == '__main__':
    app.run(debug=True)