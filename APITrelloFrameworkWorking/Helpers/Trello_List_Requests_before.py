import requests
import pytest
from requests_oauthlib import OAuth1

import APITrelloFramework
from APITrelloFramework.Configuration import urlcreation, namecreation, host_config
from APITrelloFramework.Helpers.Trello_Board_Request import test_Trello


class test_List_Trello:

    def __init__(self):
        self.Base_List_uri = urlcreation.Base_List_uri
        self.auth = OAuth1(host_config.Consumer_Key, host_config.Consumer_Secret, host_config.Access_Token,
                           host_config.Token_Secret)
        self.List_get_uri = urlcreation.List_get_uri
        self.List_rename_uri = urlcreation.List_rename_uri
        self.List_del_uri = urlcreation.List_del_uri
        self.query_param = namecreation.List_query_param
       # self.boardid=APITrelloFramework.Helpers.Trello_Board_Request.test_Trello

    @pytest.mark.get_trello
    def test_create_list(self,board_id):
        self.query_param = self.query_param
        List_response = requests.post(self.Base_List_uri, params=self.query_param + board_id, auth=self.auth)
        #print(List_response.url)
        #print("List Response:", List_response)
        return List_response

    @pytest.mark.get_trello
    def test_get_list(self, list_id):
        get_list = requests.get(self.test_get_list + list_id, auth=self.auth)
        return get_list

    @pytest.mark.upd_trello
    def test_update_list(self, query_param, list_id):
        upd_list = requests.put(self.List_rename_uri + list_id, params=query_param, auth=self.auth)
        #print("upd_list from request",upd_list)
        return upd_list

    @pytest.mark.del_trello
    def test_del_list(self, list_id):
        del_list = requests.delete(self.List_del_uri + list_id, auth=self.auth)
        print("Delete from Request:",del_list.url)
        return del_list



