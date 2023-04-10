import requests
import json
from pprint import pprint
request_uri='http://petstore.swagger.io/#/'
request_payload={
  "id": 12345,
  "category": {
    "id": 1,
    "name": "dog"
  },
  "name": "snoopie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "pending"
}

response=requests.post(request_uri,data=request_payload)
print(response.status_code)

'''import json
from pprint import pprint
request_uri='https://petstore.swagger.io/v2/pet/12345'
response=requests.get(request_uri)
#print(response.status_code)
#Verify that status code is 200
assert response.status_code==200,'AssertionError'
print(response.headers)
print(response.headers.get('Content-Type'))
assert (response.headers.get('Content-Type'))=='application/json', 'AssertionError'
pprint(response.json())
res=response.json()
print(res['name'])'''