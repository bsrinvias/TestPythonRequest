import jsonpath
import requests, json, pytest
from requests_oauthlib import oauth1_auth
from requests_oauthlib import OAuth1
from pprint import pprint
requests_uri = 'https://api.trello.com/1/boards/'
query_param='name=TEST'
auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
                  '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988',
                  'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46', '')
response = requests.post(requests_uri,params=query_param, auth=auth)
print(response)
res1 = response.text
print(res1)
#get_Board_id = res1['id']
#pprint(res1)
res2=json.loads(res1)
res3=jsonpath.jsonpath("res2",id)
print(res2)
print(res3)


