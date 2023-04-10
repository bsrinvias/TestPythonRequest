import requests, json, jsonpath

requests_uri = 'https://jsonplaceholder.typicode.com/users/1'
response = requests.get(requests_uri)
response_body = response.json()