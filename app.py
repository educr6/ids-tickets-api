from flask import Flask
from flask import request
import flask
from json_db_client import JsonDbClient



app = Flask(__name__)

@app.route('/')
def hello_world():
    return {"hello": "world"}


@app.route('/ticket', methods=["GET", 'POST'])
def tickets():

    db_client = JsonDbClient('./tickets_db.json')


    if (flask.request.method == "GET"):
        return {
            "meta": {
                "test": "test"
            },
            "data": db_client.get_tickets()
        }
    
    if (flask.request.method == "POST"):

        new_ticket = request.json

        return {
            "meta": {
                "test": "test"
            },
            "data": db_client.create_ticket(new_ticket)
        }

    

@app.route('/ticket/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_ticket(id):

    db_client = JsonDbClient('./tickets_db.json')

    if (flask.request.method == 'GET'):
        return {
            "meta": {
                "test": "test"
            },
            "data": db_client.get_ticket_by_id(id)
        }
    
    if (flask.request.method == 'PUT'):
        
        updated_ticket = request.json
        
        return {
            "meta": {
                "test": "test"
            },
            "data": db_client.update_ticket(id, updated_ticket)

        }
    
    if (flask.request.method == "DELETE") :

        return {
            "meta": {
                "test": "test"
            },
            "data": db_client.delete_ticket(id)
        }

    

    



if __name__ == '__main__':
    app.run(debug=True)