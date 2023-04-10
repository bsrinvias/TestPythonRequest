#https://www.google.com/search?q=API+Automation+using+python+youtube&rlz=1C1GCEU_enIN941IN941&oq=API+Automation+using+python+youtube&aqs=chrome..69i57j0i546l2j69i64.16608j0j7&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:28ef6a0d,vid:YeAWDfxqD7g
import requests,json,jsonpath

# check that status code is 200
def test_status_code_200():
    requests_uri='https://jsonplaceholder.typicode.com/users/1'
    response=requests.get(requests_uri)
    assert response.status_code==200
def test_header_content():
    requests_uri = 'https://jsonplaceholder.typicode.com/users/1'
    response = requests.get(requests_uri)
    assert response.headers['Content-Type']=="application/json; charset=utf-8"
    print(response.headers.get('Content-Type'))
def test_name_content():
    requests_uri = 'https://jsonplaceholder.typicode.com/users/1'
    response = requests.get(requests_uri)
    response_body=response.json()
    assert "name" in response_body
def test_name_one():
    requests_uri = 'https://jsonplaceholder.typicode.com/users/1'
    response = requests.get(requests_uri)
    response_body = response.json()
    assert response_body['name']=='Leanne Graham'
def test_name_one():
    requests_uri = 'https://jsonplaceholder.typicode.com/users/1'
    response = requests.get(requests_uri)
    response_body = response.json()
    print(response_body)
    assert response_body['company']['name']=='Romaguera-Crona'
def test_name_countusers():
    requests_uri = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(requests_uri)
    response_body = response.json()
    assert len(response_body)==10
def test_add_new_user():
    my_new_body={"id":1,"name":"abc","body":"test"}
    requests_uri = 'https://jsonplaceholder.typicode.com/users/posts'
    response = requests.post(requests_uri,json=my_new_body)
    assert response.status_code==201


