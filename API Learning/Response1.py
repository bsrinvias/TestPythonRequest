import json

import requests
request_uri='https://reqres.in/api/users?page=2'
response=requests.get(request_uri)
print(response.json())
#convert from json into dictionary
json_res=json.loads(response.text)
print(type(json_res))
print(json_res['page']==2)
assert (json_res['page']==2),"AssertionError"
res_data=json_res['data']
#List in the dictionary
assert (res_data[0]['id'])==7,"AssertionError"

def get_res_data():
    for x in res_data:
        print(x['id'])


#Header
res_head=response.headers
print((res_head))
print(res_head.get('Date'))
print(res_head.get('Content-Type'))