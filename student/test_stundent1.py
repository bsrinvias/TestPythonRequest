import requests,json,jsonpath
requests_uri='https://jsonplaceholder.typicode.com/users/1'
response = requests.get(requests_uri)
response_body = response.json()


# check that status code is 200
def test_status_code_200():
    assert response.status_code==200
def test_header_content():
    assert response.headers['Content-Type']=="application/json; charset=utf-8"
def test_name_content():
    assert "name" in response_body
def test_name_one():
    assert response_body['name']=='Leanne Graham'
def test_name_one():
    assert response_body['company']['name']=='Romaguera-Crona'
def test_name_countusers():
    requests_uri = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(requests_uri)
    response_body = response.json()
    assert len(response_body)==10





'''def test_add_new_user():
    my_new_body={"id":1,"name":"abc","body":"test"}
    requests_uri = 'https://jsonplaceholder.typicode.com/users/posts'
    response = requests.post(requests_uri,json=my_new_body)
    assert response.status_code==201'''


