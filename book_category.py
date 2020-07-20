from flask_restful import Resource

categories = ['Finance', 'Education', 'Action', 'Programing']

class Category(Resource):
    def get(self):
        return categories