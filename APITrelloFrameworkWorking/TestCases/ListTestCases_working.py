from APITrelloFramework.Configuration import namecreation
from APITrelloFramework.Helpers.Trello_Board_Request import test_Trello
from APITrelloFramework.Helpers.Trello_List_Requests_before import test_List_Trello


def test_list_board():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = test_List_Trello()
    new_list = test_list.test_create_list(board_id)
    assert new_list.status_code == 200, "List creation unsuccessful"
    res2 = new_list.json()
    list_id = res2['id']


def test_get_list():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = test_List_Trello()
    get_list = test_list.test_create_list(board_id)
    assert get_list.status_code == 200, "Fetch List unsuccessful"
    res2 = get_list.json()
    list_id = res2['id']


def test_update_list():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = test_List_Trello()
    new_list = test_list.test_create_list(board_id)
    assert new_list.status_code == 200, "List rename unsuccessful"
    res2 = new_list.json()
    list_id = res2['id']
    query_param = namecreation.New_List_Name
    update_list = test_list.test_update_list(query_param, list_id)
    assert update_list.status_code == 200, "List Deletion unsuccessful"


def test_del_list():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = test_List_Trello()
    new_list = test_list.test_create_list(board_id)
    assert new_list.status_code == 200, "List creation unsuccessful"
    res2 = new_list.json()
    list_id = res2['id']
    del_list = test_list.test_del_list(list_id)
