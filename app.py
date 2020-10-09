from flask import Flask
from flask import request
import flask
import sandbox



app = Flask(__name__)

@app.route('/')
def hello_world():
    return {"hello": "world"}


@app.route('/ticket', methods=["GET", 'POST'])
def tickets():

    if (flask.request.method == "GET"):
        return {
            "meta": {
                "test": "test"
            },
            "data": sandbox.get_tickets()
        }
    
    if (flask.request.method == "POST"):

        new_ticket = request.json
        
        return {
            "meta": {
                "test": "test"
            },
            "data": sandbox.create_ticket(new_ticket)
        }

    

@app.route('/ticket/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_ticket(id):

    if (flask.request.method == 'GET'):
        return {
            "meta": {
                "test": "test"
            },
            "data": sandbox.get_ticket_by_id(id)
        }
    
    if (flask.request.method == 'PUT'):
        
        updated_ticket = request.json
        
        return {
            "meta": {
                "test": "test"
            },
            "data": sandbox.update_ticket(id, updated_ticket)

        }
    
    if (flask.request.method == "DELETE") :

        return {
            "meta": {
                "test": "test"
            },
            "data": sandbox.delete_ticket(id)
        }

    

    



if __name__ == '__main__':
    app.run(debug=True)