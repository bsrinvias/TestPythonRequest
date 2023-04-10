import requests
import json
import jsonpath
from requests_oauthlib import OAuth1
import pytest
from APITrelloFramework.Configuration import urlcreation, namecreation, host_config
#from Trello_Practice.CreateBoard import upd_board
import logging
import allure
import allure_pytest

create_Board_uri=urlcreation.Board_create_uri
print(create_Board_uri)
class test_Trello:


    def __init__(self):
        self.requests_uri = urlcreation.Board_create_uri
        self.auth=OAuth1(host_config.Consumer_Key,host_config.Consumer_Secret,host_config.Access_Token,host_config.Token_Secret)
        self.get_Board_uri = urlcreation.Board_get_uri
        self.rename_Board_uri = urlcreation.Board_rename_uri
        self.del_Board_uri = urlcreation.Board_del_uri
        self.query_param=namecreation.Board_query_param



    @pytest.mark.create_trello
    def test_create_board(self):
      #  query_param = 'name=ABC_1'
        print(self.query_param)
        response = requests.post(self.requests_uri,params=self.query_param, auth=self.auth)
        print(f'status code for get Board:{response.status_code}')
        #print(response.url)
        res1 = response.json()
        global get_Board_id
        get_Board_id = res1['id']
        print(get_Board_id)
        self.get_Board_id=get_Board_id
        #global Boardid
        #Boardid= get_Board_id
        # print('*******')
        # self.query_param=self.query_param+get_Board_id
        return get_Board_id





    @pytest.mark.get_trello
    def test_get_board(self):
        get_board = requests.get(self.get_Board_uri + get_Board_id, auth=self.auth)
        assert get_board.status_code == 200, "Get Board Response code is incorrect"
        print(f'status code for get Board:{get_board.status_code}')

    @pytest.mark.upd_trello
    def test_update_board(self):
        query_param = 'name=TESTtest3'
        upd_board = requests.put(self.rename_Board_uri + get_Board_id, params=query_param, auth=self.auth)
        assert upd_board.status_code == 200, "Update Board Response code is incorrect"
        print(f'Status code for Rename Board : {upd_board.status_code}')

    @pytest.mark.del_trello
    def test_del_board(self):
        del_board = requests.delete(self.get_Board_uri + get_Board_id, auth=self.auth)
        assert del_board.status_code == 200, "Delete Board Response code is incorrect"
        print(f'Status Code for Delete Board:{del_board.status_code}')









