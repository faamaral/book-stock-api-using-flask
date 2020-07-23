import json

from flask import Flask, request
from flask_restful import Resource, Api
from .models import Authors, Categories, Books

app = Flask(__name__)
api = Api(app)

class Category(Resource):
    def get(self, id):
        category = Categories.query.filter_by(id=id).first()
        try:
            response = {
                'id': category.id,
                'category': category.category
            }
        except AttributeError:
            response = {
                'status': 'ERROR'
            }
        return response
    def put(self, id):
        category = Categories.query.filter_by(id=id).first()
        data = request.json
        if 'id' in data:
            category.id = data['id']
        if 'category' in data:
            category.category = data['category']
        category.save()
        response = {
            'id': category.id,
            'category': category.category
        }
        return response
    def delete(self, id):
        category = Categories.query.filter_by(id=id).first()
        category.delete()
        return {
            'status': 'success'
        }

class List_Categories():
    def post(self):
        data = request.json
        category = Categories(id=data['id'], category=data['category'])
        category.save()
        response = {
            'id': category.id,
            'category': category.category
        }
        return response

    def get(self):
        category = Categories.query.all()
        response = [{
            'id': i.id,
            'category': i.category
        } for i in category]
        return response

class Author(Resource):
    def put(self, cpf):
        author = Authors.query.filter_by(cpf=cpf).first()
        #data = json.loads(request.data)
        data = request.json
        if 'cpf' in data:
            author.cpf = data['cpf']
        if 'name' in data:
            author.name = data['name']
        author.save()
        response = {
            'cpf': author.cpf,
            'name': author.name
        }
        return response


    def get(self, cpf):
        author = Authors.query.filter_by(cpf=cpf).first()
        try:
            response = {
                'cpf': author.cpf,
                'name': author.name
            }
        except AttributeError:
            response = {
                'Message': 'atribute didnt found'
            }
        return response

    def delete(self, cpf):
        author = Authors.query.filter_by(cpf=cpf).first()
        author.delete()
        return {
            'status': 'success'
        }

class List_Authors():
    def post(self):
        data = request.json
        author = Authors(cpf=data['cpf'], name=data['name'])
        author.save()
        response = {
            'cpf': author.cpf,
            'name': author.name
        }
        return response

    def get(self):
        author = Authors.query.all()
        response = [{
            'cpf': i.cpf,
            'name': i.name
        } for i in author]
        return response

class List_Books(Resource):
    def get(self):
        books = Books.query.all()
        response = [{
            'id': i.id,
            'title': i.title,
            'author': i.author_cpf.name,
            'category': i.category_id.category,
            'year': i.year,
            'amount': i.amount,
            'price': i.price

        } for i in books]
    def post(self):
        data = request.json
        author = Authors.query.filter_by(cpf=data['author_cpf']).first()
        category = Categories.query.filter_by(id=data['category_id']).first()
        book = Books(title=data['title'], author_cpf=author, category_id=category, year=data['year'], amount=data['amount'], price=data['price'])
        book.save()
        response={
            'id': book.id,
            'title': book.title,
            'author': book.author_cpf.cpf
        }
        return response



api.add_resource(List_Categories, '/category/')
api.add_resource(Category, '/category/<int:id>')
api.add_resource(List_Authors, '/author/')
api.add_resource(Author, '/author/<string:cpf>')
api.add_resource(List_Books, '/books/')

if __name__ == '__main__':
    app.run(debug=True)