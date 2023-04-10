import requests
from requests_oauthlib import OAuth1
class Request:
    def __init__(self, request_url, query_param,auth_token):
        self.request_url = request_url,
        self.auth_token = auth_token,
        self.query_params = query_param

    def response(self):
        requests_uri = 'https://api.trello.com/1/boards/'
        query_param = 'name=TEST'
        auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
                      '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988',
                      'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46', '')
        print("*************in response methon*********")
        print(self.request_url, self.query_params, self.auth_token)
        response = requests.post(requests_uri, params=query_param,auth=auth)
        print(response)

"""auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
                  '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988',
                  'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46', '')
requests_uri = 'https://api.trello.com/1/boards/'
query_param='name=TEST'"""

req1 = Request(requests_uri, query_param, auth)
req1.response()