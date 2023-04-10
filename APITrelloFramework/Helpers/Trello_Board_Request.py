import requests
import pytest
from requests_oauthlib import OAuth1
from APITrelloFramework.Configuration import urlcreation, namecreation, host_config


class Trello_Board:
    def __init__(self):
        self.Base_Board_uri = urlcreation.Base_Board_uri
        self.auth = OAuth1(host_config.Consumer_Key, host_config.Consumer_Secret, host_config.Access_Token,
                           host_config.Token_Secret)
        self.query_param = namecreation.Board_query_param

    def Create_Board(self):
        cre_board_res = requests.post(self.Base_Board_uri, params=self.query_param, auth=self.auth)
        return cre_board_res

    def Get_Board(self, board_id):
        get_board_res = requests.get(self.Base_Board_uri + board_id, auth=self.auth)
        return get_board_res

    def Update_Board(self, query_param, board_id):
        upd_board_res = requests.put(self.Base_Board_uri + board_id, params=query_param, auth=self.auth)
        return upd_board_res

    def Del_Board(self, board_id):
        del_board_res = requests.delete(self.Base_Board_uri + board_id, auth=self.auth)
        return del_board_res
