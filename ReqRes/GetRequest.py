import jsonpath
import requests
import json
#request_uri='https://reqres.in/api/users?page=2'
request_uri='https://reqres.in/api/unknown'
response=requests.get(request_uri)
res_json=response.json()
print(res_json)
print(response.content)
#print(response.headers.get('Content-Type'))
response_json1=json.loads(response.text)
pages=jsonpath.jsonpath(response_json1,'total_pages')
print(pages[0])
