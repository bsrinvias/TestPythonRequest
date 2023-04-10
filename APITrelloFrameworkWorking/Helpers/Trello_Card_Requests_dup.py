import requests
import json
import jsonpath
from requests_oauthlib import OAuth1
import pytest

import APITrelloFramework
from APITrelloFramework.Configuration import urlcreation, namecreation, host_config
from Trello_Practice.CreateBoard import upd_board
from APITrelloFramework.Helpers.Trello_Board_Request import test_Trello


class test_List_Trello:
    get_Card_id=0
    def __init__(self):
        self.requests_uri = urlcreation.Card_create_uri
        self.auth=OAuth1(host_config.Consumer_Key,host_config.Consumer_Secret,host_config.Access_Token,host_config.Token_Secret)
        self.Card_get_uri= urlcreation.Card_get_uri
        self.Card_rename_uri = urlcreation.Card_rename_uri
        self.Card_del_uri = urlcreation.Card_del_uri
        self.query_param=namecreation.query_param
        self.query_param1=APITrelloFramework.Helpers.Trello_Board_Request.test_create_board.get_Board_id
    @pytest.mark.create_trello
    def test_create_card(self):
        query_param = 'name=List'
        Card_response = requests.post(self.requests_uri, params=query_param + self.query_param1,
        auth=self.auth)
        print(Card_response.url)
        print(Card_response.url)
        res1 = Card_response.json()
        global get_Card_id
        get_Card_id = res1['id']
        return get_Card_id

    @pytest.mark.get_trello
    def test_get_card(self):
        get_card = requests.get(self.Card_get_uri + get_Card_id, auth=self.auth)
        assert get_card.status_code == 200, "Get Board Response code is incorrect"
        print(f'status code for get Board:{get_card.status_code}')

    @pytest.mark.upd_trello
    def test_update_card(self):
        query_param = 'name=TESTtest3'
        rename_card = requests.put(self.Card_rename_uri + get_Card_id, params=query_param, auth=self.auth)
        assert rename_card.status_code == 200, "Update Board Response code is incorrect"
        print(f'Status code for Rename Board : {rename_card.status_code}')

    @pytest.mark.del_trello
    def test_del_card(self):
        del_card = requests.delete(self.Card_del_uri + get_Card_id, auth=self.auth)
        assert del_card.status_code == 200, "Delete Board Response code is incorrect"
        print(f'Status Code for Delete Board:{del_card.status_code}')









