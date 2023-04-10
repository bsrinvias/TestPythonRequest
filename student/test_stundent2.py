import requests,json,jsonpath
class first():
    '''requests_uri='https://jsonplaceholder.typicode.com/users/1'
    response = requests.get(requests_uri)
    response_body = response.json()'''

    def __init__(self):
        self.requests_uri = 'https://jsonplaceholder.typicode.com/users/1'
        self.response = requests.get(self.requests_uri)
        self.response_body = self.response.json()
    # check that status code is 200
    def test_status_code_200(self):
            assert self.response.status_code==200
    '''def test_header_content(self):
            assert self.response_body.headers['Content-Type']=="application/json; charset=utf-8"'''







