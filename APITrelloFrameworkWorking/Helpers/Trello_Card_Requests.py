import requests
import pytest
from requests_oauthlib import OAuth1

import APITrelloFramework
from APITrelloFramework.Configuration import urlcreation, namecreation, host_config
from APITrelloFramework.Helpers.Trello_Board_Request import test_Trello


class test_card_Trello:

    def __init__(self):
        self.Base_Card_uri = urlcreation.Base_Card_uri
        self.auth = OAuth1(host_config.Consumer_Key, host_config.Consumer_Secret, host_config.Access_Token,
                           host_config.Token_Secret)
        self.Card_get_uri = urlcreation.Card_get_uri
        self.Card_rename_uri = urlcreation.Card_rename_uri
        self.Card_del_uri = urlcreation.Card_del_uri
        self.query_param = namecreation.Card_query_param

    @pytest.mark.get_trello
    def test_create_card(self, list_id):
        self.query_param = self.query_param
        card_response = requests.post(self.Base_Card_uri, params=self.query_param + list_id, auth=self.auth)
        return card_response

    @pytest.mark.get_trello
    def test_get_card(self, card_id):
        get_card = requests.get(self.Card_get_uri + card_id, auth=self.auth)
        return get_card

    @pytest.mark.upd_trello
    def test_update_card(self, query_param, card_id):
        upd_card = requests.put(self.Card_rename_uri + card_id, params=query_param, auth=self.auth)
        return upd_card

    @pytest.mark.del_trello
    def test_del_card(self, card_id):
        del_card = requests.delete(self.Card_del_uri + card_id, auth=self.auth)
        return del_card
