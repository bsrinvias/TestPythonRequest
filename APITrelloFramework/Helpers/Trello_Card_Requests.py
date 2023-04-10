import requests
import pytest
from requests_oauthlib import OAuth1
from APITrelloFramework.Configuration import urlcreation, namecreation, host_config


class Trello_Card:

    def __init__(self):
        self.Base_Card_uri = urlcreation.Base_Card_uri
        self.auth = OAuth1(host_config.Consumer_Key, host_config.Consumer_Secret, host_config.Access_Token,
                           host_config.Token_Secret)
        self.Card_get_uri = urlcreation.Card_get_uri
        self.Card_rename_uri = urlcreation.Card_rename_uri
        self.Card_del_uri = urlcreation.Card_del_uri
        self.query_param = namecreation.Card_query_param

    def Create_Card(self, list_id):
        self.query_param = self.query_param
        cre_card_response = requests.post(self.Base_Card_uri, params=self.query_param + list_id, auth=self.auth)
        return cre_card_response

    def Get_Card(self, card_id):
        get_card_res = requests.get(self.Card_get_uri + card_id, auth=self.auth)
        return get_card_res

    def Update_Card(self, query_param, card_id):
        upd_card_res = requests.put(self.Card_rename_uri + card_id, params=query_param, auth=self.auth)
        return upd_card_res

    def Del_Card(self, card_id):
        del_card_res = requests.delete(self.Card_del_uri + card_id, auth=self.auth)
        return del_card_res
