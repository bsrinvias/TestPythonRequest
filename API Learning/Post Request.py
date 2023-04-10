from datetime import date

import requests

print("Script Run Date:",date.today())
request_uri='https://jsonplaceholder.typicode.com/posts/'
requests_param=''
requests_header={'Content-Type':'application/json'}
requests_auth=''
response=requests.get(request_uri,headers=requests_header)
print("Response code:",response.status_code,"response text:",response.reason)
print(response.json())
res=response.json()
for i in range(len(res)):
    print(res[i])