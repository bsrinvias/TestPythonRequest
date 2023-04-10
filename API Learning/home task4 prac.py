import json
from itertools import count


import requests
from pprint import pprint
request_uri='https://jsonplaceholder.typicode.com/users'
response=requests.get(request_uri)
#pprint(response.json())
print("Verify the status code:",response.status_code)
assert response.status_code==200,'AssertionError'
res1=response.json()
#print(res1)
print("Verify the count of users:",(len(res1)))
print("Name:",res1[1]['name'])
'''count=0
for i in range(len(res1)):
    if res1[i]['name']== "Ervin Howell":
       print("id:",res1[i]['id'],"'Ervin Howel' exists")
       count = count+1
if count>0:
    print("No of time name exist:",count)
    print("exist")
else:
    print("does not exist")'''


pprint(res1[0])

print(type(res1))
print(res1[0].count('Leanne Graham'))
#print(list1.count(4))



