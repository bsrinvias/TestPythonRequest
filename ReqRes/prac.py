import requests
from requests_oauthlib import oauth1_auth
from requests_oauthlib import OAuth1
requests_uri='https://api.trello.com/1/boards/?name=TEST'
auth=OAuth1('e8a0e2dd807820e641f0960bd3821077',
              '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988', 'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46','')

response=requests.post(requests_uri,auth=auth)
res1=response.json()
get_Board_id=res1['id']
assert response.status_code==200,"Create Board Response code is incorrect"

get_Board_uri='https://api.trello.com/1/boards/'
get_board=requests.get(get_Board_uri+get_Board_id,auth=auth)
assert get_board.status_code==200,"Get Board Response code is incorrect"

upd_Board_uri='https://api.trello.com/1/boards/'
query_param='name=TESTtest3'
upd_board=requests.put(get_Board_uri+get_Board_id,params=query_param,auth=auth)
assert upd_board.status_code==200,"Update Board Response code is incorrect"


del_Board_uri='https://api.trello.com/1/boards/'
del_board=requests.delete(get_Board_uri+get_Board_id,auth=auth)
assert upd_board.status_code==200,"Delete Board Response code is incorrect"
