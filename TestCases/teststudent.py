import requests
import json
import jsonpath
request_uri='https://thetestingworldapi.com/api/studentsDetails/123'
response=requests.get(request_uri)
print(response.status_code)
print(type(response))
'''print(response.headers.get('Content-Type'))
res_json=json.loads(response)
res2=jsonpath.jsonpath(res_json)
print(res2)'''
