import requests
import json
from pprint import pprint
request_uri='https://petstore.swagger.io/v2/pet/12345'
response=requests.get(request_uri)
res=response.json()
print(response.json())
print("Pet Name:",res['category']['name'])
print("Name of the pet:",res['name'])
print("Current Status:",res['status'])
pet= (res['category']['name'])
if pet=='dog':
    assert res['name']=='snoopie','AssertionError'
    assert res['status']=='pending','AssertionError'








