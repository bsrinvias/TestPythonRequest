import requests
import json,jsonpath
from pprint import pprint

requests_uri=('https://www.zippopotam.us/de/24848#places/3')
response=requests.get(requests_uri)
print(f'status code:{response.status_code}')
print(f'Header: {response.headers}')
print(f'Response Body:{response.content}')
print(json.dumps(response.json(),indent=4))