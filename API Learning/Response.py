import requests
request_uri='https://jsonplaceholder.typicode.com/posts'
response=requests.get(request_uri)
print(response.status_code==requests.codes.ok)
print(response.status_code)
print(response.content) #byte format
print(response.text) #raw format/uni code
print(response.json()) #json format
print(response.raise_for_status()) #if any error will show
print(response.encoding) #encoding passed
print(response.headers) #header details
print(response.headers.get('Date')) #to get particular header
print(response.url)
