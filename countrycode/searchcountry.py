import requests
import json,jsonpath
from pprint import pprint

requests_uri=('https://www.zippopotam.us/de/24848#places/3')
response=requests.get(requests_uri)
print(response.status_code)
response_body=response.json()
pprint(response_body)
print(response_body['country'])
print(response_body['country abbreviation'])
print(response_body['places'])
print(response_body['places'][0]['place name'])
print(response_body['places'][1]['place name'])
print(response_body['places'][2]['place name'])
print(response_body['places'][3]['place name'])
print(response_body['post code'])