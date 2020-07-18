from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route("/<int:id>")

def book(id):
    return jsonify({'id': id, 'title': 'Test'})

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