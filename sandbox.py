import json
import random
import pprint
import string

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

def generate_code():

    first_two_digits = random.randint(11,99)
    four_characters = get_random_string(4)

    code = "%s-%s" % (first_two_digits, four_characters)
    return code
    

def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str.upper()



def id_exists(id):
    
    phantom_ticket = get_ticket_by_id(id)
    return phantom_ticket != {}

def get_current_date_string():
    return 



def create_ticket(ticket):
    
    ticket_id = random_number()
    id_existence = id_exists(ticket_id)

    while id_existence :
        ticket_id = random_number()
        id_existence  = id_exists(ticket_id)
    
    ticket["id"] = ticket_id
    ticket["code"] = generate_code()

    data = get_tickets()
    data.append(ticket)
    write_file(data)

    return ticket


def delete_ticket(id):

    tickets = get_tickets()
    ticket_to_delete = get_ticket_by_id(id)

    tickets.remove(ticket_to_delete)
    write_file(tickets)

    return ticket_to_delete

def update_ticket(id, new_ticket_info):

    tickets = get_tickets()
    updated_ticket = {}
    
    for single_ticket in tickets:
        
        if (single_ticket["id"] == id):

            single_ticket["name"] = new_ticket_info["name"]
            single_ticket["type"] = new_ticket_info["name"]
            single_ticket["status"] = new_ticket_info["name"]

            updated_ticket = single_ticket
    
    write_file(tickets)

    return updated_ticket
            

            




    return




pp = pprint.PrettyPrinter(indent=4)
print("TICKETS INITIALLY")
pp.pprint(get_tickets())


print("DELETED TICKET")
pp.pprint(delete_ticket(256))
print("NEW LIST")
pp.pprint(get_tickets())









