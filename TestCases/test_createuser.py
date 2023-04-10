import requests
import json

def test_create_user1():
    request_uri='https://reqres.in/api/users'
    data={"name": "morpheus",
        "job": "leader" }
    response=requests.post(request_uri,data=data)
    assert response.status_code==202
def test_Create_user2():
    request_uri = 'https://reqres.in/api/users'
    data = {"name": "morpheus1",
            "job": "leader1"}
    response = requests.post(request_uri, data=data)
    assert response.status_code == 201


