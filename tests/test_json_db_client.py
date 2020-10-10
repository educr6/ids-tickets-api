
def test_write_json(json_db_client):
    expected = [{"id": 1, "code": "20-AD356", "name": "Esta es la prueba", "type": "Bug", "status": "en progreso", "submission-date": "2015-03-25", "details": "generic details"}, {"id": 2, "code": "21-LBJ356", "name": "Consulta de fecha de corte crash", "type": "Issue", "status": "cerrado", "submission-date": "2015-03-28", "details": "generic details"}]
    json_db_client.write_file(expected)

    assert expected == json_db_client.get_tickets()

def test_get_single_ticket1(json_db_client):

    expected = {"id": 1, "code": "20-AD356", "name": "Esta es la prueba", "type": "Bug", "status": "en progreso", "submission-date": "2015-03-25", "details": "generic details"}

    assert expected == json_db_client.get_ticket_by_id(1)

def test_get_single_ticket2(json_db_client):

    expected = {"id": 2, "code": "21-LBJ356", "name": "Consulta de fecha de corte crash", "type": "Issue", "status": "cerrado", "submission-date": "2015-03-28", "details": "generic details"}

    assert expected == json_db_client.get_ticket_by_id(2)

def test_id_exists(json_db_client):
    expected = True
    assert expected == json_db_client.id_exists(1)
    assert expected == json_db_client.id_exists(2)

def test_update_ticket(json_db_client):

    expected = {"id": 2, "code": "21-LBJ356", "name": "Modificado por pruebas", "type": "Issue", "status": "cerrado", "submission-date": "2015-03-28", "details": "generic details modificados"}

    assert expected == json_db_client.update_ticket(expected["id"], {"name": "Modificado por pruebas", "type": "Issue", "status": "cerrado", "submission-date": "2015-03-28", "details": "generic details modificados"})

def test_delete_ticket(json_db_client):

    expected = False
    expected_count = 1

    json_db_client.delete_ticket(2)

    assert expected == json_db_client.id_exists(2)
    assert expected_count == len(json_db_client.get_tickets())