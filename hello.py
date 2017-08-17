from flask import Flask, request
from flask.ext.api import status
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/income-statements?start_index=<int:index>&limit=<int:limit>',
           methods=['GET'])
def get(index, limit):
    if request.method == 'GET':
        return '[id1, id2, id3], 200\n'


# e.g. curl -vX PUT http://127.0.0.1:5000/income-statements/3
@app.route('/income-statements/<int:statement_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def post(statement_id):
    if request.method == 'POST':
        print('posted new id, ' + str(statement_id) + '\n')
        return 'posted new id, ' + str(statement_id) + '\n', status.HTTP_201_CREATED
    if request.method == 'PUT':
        print('put new id, ' + str(statement_id) + '\n')
        return 'put new id, ' + str(statement_id) + '\n', status.HTTP_204_NO_CONTENT
    if request.method == 'DELETE':
        print('deleted an id, ' + str(statement_id) + '\n')
        return 'deleted an id, ' + str(statement_id) + '\n', status.HTTP_204_NO_CONTENT
    else:
        return 'get works, id: ' + str(statement_id) + '\n', status.HTTP_200_OK


@app.route('/put/')
def put():
    return '204\n'


@app.route('/delete/')
def delete():
    return '204\n'

