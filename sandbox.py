import json
import random
import pprint

def read_file():
    
    with open('./tickets_db.json') as f:
        data = json.load(f)
    
    return data
    


def write_file(data):

    with open('./tickets_db.json', 'w') as outfile:
        json.dump(data, outfile)



def get_tickets():
    data = read_file()
    return data



def get_ticket_by_id(id):
    data = read_file()

    for ticket in data:
        if (ticket["id"] == id):
            return ticket
    
    return {}



def random_number():
    return random.randint(1, 500)



def id_exists(id):
    
    phantom_ticket = get_ticket_by_id(id)
    return phantom_ticket != {}



def create_ticket(ticket):
    
    ticket_id = random_number()
    id_existence = id_exists(ticket_id)

    while id_existence :
        ticket_id = random_number()
        id_existence  = id_exists(ticket_id)
    
    ticket["id"] = ticket_id

    data = get_tickets()
    data.append(ticket)
    write_file(data)

    return ticket











