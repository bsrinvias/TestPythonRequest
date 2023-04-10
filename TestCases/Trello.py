import requests
import json
import jsonpath
from requests_oauthlib import oauth1_auth
from requests_oauthlib import OAuth1
request_uri='https://api.trello.com/1/boards/}'
query_param={"name=TEST"}
auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
              '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988', 'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46','')
#response=requests.post('https://api.trello.com/1/boards/?name=TEST',auth=auth)
response=requests.post(request_uri+query_param,auth=auth)
print(response.status_code)
final=response.json()
print(type(final))
print(final['id'])


