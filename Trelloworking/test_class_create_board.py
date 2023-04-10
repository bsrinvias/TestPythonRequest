import unittest
import requests
from requests_oauthlib import OAuth1

import test_create_board
from TestClass import CRUD_Operations
requests_uri = 'https://api.trello.com/1/boards/'
auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
                  '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988',
                  'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46', '')
query_params = 'name=TEST'
response = requests.post(requests_uri, auth=auth)
class TestMyClass(unittest.TestCase):
    def test_my_function(self):
        tests = CRUD_Operations(requests_uri, query_params, auth)
        tests.test_create()
        tests.test_get()
        tests.test_update_board()
        tests.test_del_board()

if __name__ == '__main__':
    unittest.main()