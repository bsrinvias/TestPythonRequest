import requests
import json
from pprint import pprint
request_uri2=('https://jsonplaceholder.typicode.com/posts/')
response2=requests.get(request_uri2)
res=response2.json()
print(type(res))
print(len(res))
print(res[0])
print(res[0]['userId'])
print(res[0].keys())
print(res[0].values())
print(res[0].items())
for i in range(len(res)):
    print((res[i]))
for i in res:
    print(i['title'])
