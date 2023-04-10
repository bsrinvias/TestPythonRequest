import requests
import json
import jsonpath
request_uri='https://reqres.in/api/users'
file=open('input.txt','r')
file_input=file.read()
response=requests.post(request_uri,data=file_input)
print(response.json())
res_json=response.json()
print(type(res_json))
print(res_json['id'])
print(res_json['createdAt'])
