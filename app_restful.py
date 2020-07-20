import json
from book_category import Category
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

books = [
    {
        "key": 0,
        "title": "Hello world",
        "author": "Nobody",
        "category": ["Education", "Programing", "Computer"],
        "published": 2015
    },
    {
        "key": 1,
        "title": "Two buildings",
        "author": "Test",
        "category": ["Education", "Enginner"],
        "published": 2017
    }
]

class Book(Resource):
    def get(self, id):
        try:
            response = books[id]
        except IndexError:
            response = {"status": "ERROR!"}
        return response

    def put(self, id):
        data = json.loads(request.data)
        books[id] = data
        return data

    def delete(self, id):
        books.pop(id)
        return {"Status": 200, "MESSAGE":"THIS BOOK HAS BEEN DELETED"}

class List_book(Resource):
    def get(self):
        return books
    def post(self):
        data = json.loads(request.data)
        pos = len(books)
        data["key"] = pos
        books.append(data)
        return books[pos]


api.add_resource(Book, '/books/<int:id>/')
api.add_resource(List_book, '/books/')
api.add_resource(Category, '/book-categories')

if __name__ == '__main__':
    app.run(debug=True)