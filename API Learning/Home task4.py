import requests
import json
from pprint import pprint
request_uri='https://jsonplaceholder.typicode.com/users'
response=requests.get(request_uri)
#pprint(response.json())
print("Verify the status code:",response.status_code)
assert response.status_code==200,'AssertionError'
res1=response.json()
print("Verify the count of users:",(len(res1)))
print("Name:",res1[1]['name'])
for i in range(len(res1)):
    isexist='False'
    if res1[i]['name']== "Ervin Howell":
       print("id:",res1[i]['id'],"'Ervin Howell' exists")
       isexist='True'
       break
if isexist=='False':
    print("Does not exist")





