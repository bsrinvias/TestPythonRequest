import requests
import json
from pprint import pprint
requests_uri=('https://reqres.in/api/users?page=2')
res=requests.get(requests_uri)
print("Status code:",res.status_code)
res1=res.json()
print(type(res1))
print("Count of Employee:",len(res1))
pprint((res1['data'][0]))







