import requests
import json
import jsonpath
from requests_oauthlib import OAuth1
import pytest

import APITrelloFramework
from APITrelloFramework.Configuration import urlcreation, namecreation, host_config
from Trello_Practice.CreateBoard import upd_board
from APITrelloFramework.Helpers.Trello_Board_Request import test_Trello

'''create_Board_uri=urlcreation.Board_create_uri
print(create_Board_uri)'''
class test_List_Trello:
    get_List_id=0
    def __init__(self):
        self.requests_uri = urlcreation.List_create_uri
        self.auth=OAuth1(host_config.Consumer_Key,host_config.Consumer_Secret,host_config.Access_Token,host_config.Token_Secret)
        self.List_get_uri= urlcreation.List_get_uri
        self.List_rename_uri = urlcreation.List_rename_uri
        self.List_del_uri = urlcreation.List_del_uri
        self.query_param=namecreation.List_query_param
        #self.query_param1=APITrelloFramework.Helpers.Trello_Board_Request.test_create_board.get_Board_id

    def test_create_list(self):
        query_param = 'name=List'
        print(self.query_param)
        self.query_param=self.query_param+str(test_Trello.get_id(self))
        print(self.query_param)
        List_response = requests.post(self.requests_uri,params=self.query_param,auth=self.auth)
        print(List_response.url)


    @pytest.mark.get_trello
    def test_get_list(self):
        get_List = requests.get(self.List_get_uri + get_List_id, auth=self.auth)
        assert get_List.status_code == 200, "Get Board Response code is incorrect"
        print(f'status code for get Board:{get_List.status_code}')

    @pytest.mark.upd_trello
    def test_update_list(self):
        query_param = 'name=TESTtest3'
        upd_List = requests.put(self.List_rename_uri + get_List_id, params=query_param, auth=self.auth)
        assert upd_List.status_code == 200, "Update Board Response code is incorrect"
        print(f'Status code for Rename Board : {upd_List.status_code}')

    @pytest.mark.del_trello
    def test_del_list(self):
        del_List = requests.delete(self.List_del_uri + get_List_id, auth=self.auth)
        assert del_List.status_code == 200, "Delete Board Response code is incorrect"
        print(f'Status Code for Delete Board:{del_List.status_code}')









