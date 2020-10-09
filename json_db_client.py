import json
import random
import pprint
import string
from datetime import datetime

class JsonDbClient:

    db_path = ""

    def __init__(self, path_to_db):
        self.db_path = path_to_db

    def read_file(self):
        
        with open(self.db_path) as f:
            data = json.load(f)
        
        return data
        


    def write_file(self, data):

        with open(self.db_path, 'w') as outfile:
            json.dump(data, outfile)



    def get_tickets(self):
        data = self.read_file()
        return data



    def get_ticket_by_id(self, id):
        data = self.read_file()

        for ticket in data:
            if (ticket["id"] == id):
                return ticket
        
        return {}



    def random_number(self):
        return random.randint(1, 500)

    def generate_code(self):

        first_two_digits = random.randint(11,99)
        four_characters = self.get_random_string(4)

        code = "%s-%s" % (first_two_digits, four_characters)
        return code
        

    def get_random_string(self, length):
        # Random string with the combination of lower and upper case
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str.upper()



    def id_exists(self, id):
        
        phantom_ticket = self.get_ticket_by_id(id)
        return phantom_ticket != {}

    def get_current_date_string(self):
        return datetime.today().strftime('%Y-%m-%d')



    def create_ticket(self, ticket):
        
        ticket_id = self.random_number()
        id_existence = self.id_exists(ticket_id)

        while id_existence :
            ticket_id = self.random_number()
            id_existence  = self.id_exists(ticket_id)
        
        ticket["id"] = ticket_id
        ticket["code"] = self.generate_code()
        ticket["submission-date"] = self.get_current_date_string()

        data = self.get_tickets()
        data.append(ticket)
        self.write_file(data)

        return ticket


    def delete_ticket(self, id):

        tickets = self.get_tickets()
        ticket_to_delete = self.get_ticket_by_id(id)

        if (ticket_to_delete == {}):
            return ticket_to_delete

        tickets.remove(ticket_to_delete)
        self.write_file(tickets)

        return ticket_to_delete
        

    def update_ticket(self, id, new_ticket_info):

        tickets = self.get_tickets()
        updated_ticket = {}
        
        for single_ticket in tickets:
            
            if (single_ticket["id"] == id):

                single_ticket["name"] = new_ticket_info["name"]
                single_ticket["type"] = new_ticket_info["type"]
                single_ticket["status"] = new_ticket_info["status"]

                updated_ticket = single_ticket
        
        self.write_file(tickets)

        return updated_ticket
            




        















