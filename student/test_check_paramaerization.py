import pytest
import requests
userlist=[
    {1,"'Leanne Graham1",
     2,"Leanne Graham",
     3,"Leanne Graham2"}
]
@pytest.mark.parametrize("userid,expectedname","userslist")
def test_name_one(userid,expectedname):
    requests_uri = f"https://jsonplaceholder.typicode.com/users/{userid}"
    response = requests.get(requests_uri)
    response_body = response.json()
    assert  response_body['name']==expectedname