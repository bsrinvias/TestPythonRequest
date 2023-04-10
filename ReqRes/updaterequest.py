import requests
import json
import jsonpath
request_uri='https://reqres.in/api/users'
file=open('input.txt','r')
file_input=file.read()
json_input=json.loads(file_input)
response=requests.post(request_uri,data=json_input)
#parse in json format
resq_json=json.loads(response.text)
cre=jsonpath.jsonpath(resq_json,'job')
print(resq_json)
print(cre)