import requests
import json
import jsonpath
from requests_oauthlib import OAuth1
import pytest
from APITrelloFramework.Configuration import urlcreation, namecreation, host_config
import logging
import allure
import allure_pytest

class test_Trello:
    def __init__(self):
        self.requests_uri = urlcreation.Board_create_uri
        self.auth = OAuth1(host_config.Consumer_Key, host_config.Consumer_Secret, host_config.Access_Token,
                           host_config.Token_Secret)
        self.get_Board_uri = urlcreation.Board_get_uri
        self.rename_Board_uri = urlcreation.Board_rename_uri
        self.del_Board_uri = urlcreation.Board_del_uri
        self.query_param = namecreation.Board_query_param

    @pytest.mark.create_trello
    def test_create_board(self):
        response = requests.post(self.requests_uri,params=self.query_param, auth=self.auth)
        return response

    @pytest.mark.get_trello
    def test_get_board(self, board_id):
        get_board = requests.get(self.get_Board_uri + board_id, auth=self.auth)
        return get_board

    @pytest.mark.upd_trello
    def test_update_board(self, query_param, board_id):
        upd_board = requests.put(self.rename_Board_uri + board_id, params=query_param, auth=self.auth)
        return upd_board

    @pytest.mark.del_trello
    def test_del_board(self, board_id):
        del_board = requests.delete(self.del_Board_uri + board_id, auth=self.auth)
        return del_board










