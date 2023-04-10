import requests
from requests_oauthlib import OAuth1

requests_uri = 'https://api.trello.com/1/boards/'
query_param='name=TEST'
final_url=(requests_uri+query_param)
auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
                  '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988',
                  'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46', '')
response = requests.post(requests_uri,params=query_param, auth=auth)

List_create_uri='https://api.trello.com/1/lists'
query_param = 'name=List'
url_cre = (List_create_uri,query_param)




url_cre =construct_url(List_create_uri, query_param)
print(type(url_cre))
print(url_cre)

