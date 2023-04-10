import requests
import pytest
from requests_oauthlib import OAuth1

import APITrelloFramework
from APITrelloFramework.Configuration import urlcreation, namecreation, host_config
from APITrelloFramework.Helpers.Trello_Board_Request import Trello_Board


class Trello_List:

    def __init__(self):
        self.Base_List_uri = urlcreation.Base_List_uri
        self.auth = OAuth1(host_config.Consumer_Key, host_config.Consumer_Secret, host_config.Access_Token,
                           host_config.Token_Secret)
        self.List_get_uri = urlcreation.List_get_uri
        self.List_rename_uri = urlcreation.List_rename_uri
        self.List_del_uri = urlcreation.List_del_uri
        self.query_param = namecreation.List_query_param

    def Create_List(self, board_id):
        self.query_param = self.query_param
        cre_list_response = requests.post(self.Base_List_uri, params=self.query_param + board_id, auth=self.auth)
        return cre_list_response

    def Get_List(self, list_id):
        get_list_res = requests.get(self.List_get_uri + list_id, auth=self.auth)
        return get_list_res

    def Update_List(self, query_param, list_id):
        upd_list_res = requests.put(self.List_rename_uri + list_id, params=query_param, auth=self.auth)
        return upd_list_res

    def Del_List(self, list_id):
        del_list_res = requests.delete(self.List_del_uri + list_id, auth=self.auth)
        return del_list_res
