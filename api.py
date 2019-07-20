import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
        {
            'id': 0,
            'name':'book1',
            'author':'auth1'
            },
        {
            'id': 1,
            'name': 'book2',
            'author': 'auth2'
            },
        {
            'id':2,
            'name': 'book3',
            'author': 'auth3'
            }
        ]

@app.route('/', methods=['GET'])
def home():
    return "Hello World"

@app.route('/api/v1/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Please provide 'id' parameter to the request"
    result = []
    for book in books:
        if book['id'] == id:
            result.append(book)
    return jsonify(result)
@app.errorhandler(404)
def page_not_found(e):
    return str(e) + "\nRequested Resorrce not found"

app.run()
