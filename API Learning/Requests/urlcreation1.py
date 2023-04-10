import requests, json, pytest
from requests_oauthlib import oauth1_auth
from requests_oauthlib import OAuth1
from pprint import pprint
import random

Final_Boar_Name1="Name="+'Board_'+str(random.randint(1,100))
print(Final_Boar_Name1)
Final_List_name1="Name="+'List'+str(random.randint(1,100))
print(Final_List_name1)


requests_uri = 'https://api.trello.com/1/boards/'
query_param='name=TEST1'
auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
                  '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988',
                  'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46', '')
response = requests.post(requests_uri,params=Final_List_name1, auth=auth)
print(response.url)
print(response.status_code)

'''
#https://api.trello.com/1/lists?name=List1&idBoard=63bd6afac914a7019d754859
req1='https://api.trello.com/1/lists'
query_param='name=List1'
auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
                  '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988',
                  'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46', '')
response = requests.post(req1,params=query_param, auth=auth)
print(response.url)'''
