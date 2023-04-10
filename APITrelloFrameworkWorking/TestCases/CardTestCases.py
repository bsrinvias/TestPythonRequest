from APITrelloFramework.Configuration import namecreation
from APITrelloFramework.Helpers.Trello_Board_Request import test_Trello
from APITrelloFramework.Helpers.Trello_List_Requests import test_List_Trello
from APITrelloFramework.Helpers.Trello_Card_Requests import test_card_Trello


def test_card_board():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = test_List_Trello()
    new_list = test_list.test_create_list(board_id)
    assert new_list.status_code == 200, "Card creation unsuccessful"
    res2 = new_list.json()
    list_id = res2['id']
    test_card=test_card_Trello()
    new_card=test_card.test_create_card(list_id)
    res3=new_card.json()
    card_id=res3['id']


def test_get_card():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = test_List_Trello()
    new_list = test_list.test_create_list(board_id)
    assert new_list.status_code == 200, "Card creation unsuccessful"
    res2 = new_list.json()
    list_id = res2['id']
    test_card = test_card_Trello()
    new_card = test_card.test_create_card(list_id)
    res3 = new_card.json()
    card_id = res3['id']


def test_update_card():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = test_List_Trello()
    new_list = test_list.test_create_list(board_id)
    assert new_list.status_code == 200, "Card creation unsuccessful"
    res2 = new_list.json()
    list_id = res2['id']
    test_card = test_card_Trello()
    new_card = test_card.test_create_card(list_id)
    res3 = new_card.json()
    card_id = res3['id']
    query_param = namecreation.New_Card_Name
    update_card = test_card.test_update_card(query_param, card_id)
    assert update_card.status_code == 200, "Card Deletion unsuccessful"


def test_del_card():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = test_List_Trello()
    new_list = test_list.test_create_list(board_id)
    assert new_list.status_code == 200, "Card creation unsuccessful"
    res2 = new_list.json()
    list_id = res2['id']
    test_card = test_card_Trello()
    new_card = test_card.test_create_card(list_id)
    res3 = new_card.json()
    card_id = res3['id']
    del_card = test_card.test_del_card(card_id)
