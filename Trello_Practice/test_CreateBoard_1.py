import requests, json, pytest
from requests_oauthlib import oauth1_auth
from requests_oauthlib import OAuth1
from pprint import pprint
def test_create():
    requests_uri = 'https://api.trello.com/1/boards/?name=TEST'
    auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
                  '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988',
                  'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46', '')
    response = requests.post(requests_uri, auth=auth)
    res1 = response.json()
    get_Board_id = res1['id']
    print(res1)
    return get_Board_id,auth

def test_get():
    get_Board_id,auth = test_create()
    get_Board_uri = 'https://api.trello.com/1/boards/'
    get_board = requests.get(get_Board_uri + get_Board_id, auth=auth)
    assert get_board.status_code == 200, "Get Board Response code is incorrect"

def test_update_board():
    get_Board_id, auth = test_create()
    upd_Board_uri = 'https://api.trello.com/1/boards/'
    query_param = 'name=TESTtest3'
    upd_board = requests.put(upd_Board_uri + get_Board_id, params=query_param, auth=auth)
    print(upd_board.url)
    assert upd_board.status_code == 200, "Update Board Response code is incorrect"

def test_del_board():
    get_Board_id, auth = test_create()
    del_Board_uri = 'https://api.trello.com/1/boards/'
    del_board = requests.delete(del_Board_uri + get_Board_id, auth=auth)
    assert del_board.status_code == 200, "Delete Board Response code is incorrect"