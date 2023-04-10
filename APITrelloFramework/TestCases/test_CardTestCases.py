from APITrelloFramework.Configuration import namecreation
from APITrelloFramework.Helpers.Trello_Board_Request import Trello_Board
from APITrelloFramework.Helpers.Trello_List_Requests import Trello_List
from APITrelloFramework.Helpers.Trello_Card_Requests import Trello_Card
import pytest


@pytest.fixture
def card_fixture():
    test_board = Trello_Board()
    new_board = test_board.Create_Board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = Trello_List()
    new_list = test_list.Create_List(board_id)
    res2 = new_list.json()
    list_id = res2['id']
    test_card = Trello_Card()
    new_card = test_card.Create_Card(list_id)
    res3 = new_card.json()
    card_id = res3['id']
    return new_card, test_card, test_board, board_id, card_id


def test_card_board(card_fixture):
    '''test_board = Trello_Board()
    new_board = test_board.Create_Board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = Trello_List()
    new_list = test_list.Create_List(board_id)
    res2 = new_list.json()
    list_id = res2['id']
    test_card = Trello_Card()
    new_card = test_card.Create_Card(list_id)
    res3 = new_card.json()
    card_id = res3['id']'''
    assert card_fixture[0].status_code == 200, "Card creation unsuccessful"
    del_board = card_fixture[2].Del_Board(card_fixture[3])


@pytest.mark.get_trello
def test_get_card(card_fixture):
    '''test_board = Trello_Board()
    new_board = test_board.Create_Board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = Trello_List()
    new_list = test_list.Create_List(board_id)
    res2 = new_list.json()
    list_id = res2['id']
    test_card = Trello_Card()
    new_card = test_card.Create_Card(list_id)
    res3 = new_card.json()
    card_id = res3['id']'''
    assert card_fixture[0].status_code == 200, "Card Retrieval unsuccessful"
    del_board = card_fixture[2].Del_Board(card_fixture[3])


@pytest.mark.upd_trello
def test_update_card(card_fixture):
    '''test_board = Trello_Board()
    new_board = test_board.Create_Board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = Trello_List()
    new_list = test_list.Create_List(board_id)
    res2 = new_list.json()
    list_id = res2['id']
    test_card = Trello_Card()
    new_card = test_card.Create_Card(list_id)
    res3 = new_card.json()
    card_id = res3['id']'''
    query_param = namecreation.New_Card_Name
    update_card = card_fixture[1].Update_Card(query_param, card_fixture[4])
    assert update_card.status_code == 200, "Card Rename unsuccessful"
    del_board = card_fixture[2].Del_Board(card_fixture[3])


@pytest.mark.del_trello
def test_del_card(card_fixture):
    '''test_board = Trello_Board()
    new_board = test_board.Create_Board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = Trello_List()
    new_list = test_list.Create_List(board_id)
    res2 = new_list.json()
    list_id = res2['id']
    test_card = Trello_Card()
    new_card = test_card.Create_Card(list_id)
    res3 = new_card.json()
    card_id = res3['id']'''
    del_card = card_fixture[1].Del_Card(card_fixture[4])
    assert del_card.status_code == 200, "Card Deletion is unsuccessful"
    del_board = card_fixture[2].Del_Board(card_fixture[3])
