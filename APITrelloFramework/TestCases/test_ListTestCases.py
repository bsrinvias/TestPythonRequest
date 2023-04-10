from APITrelloFramework.Configuration import namecreation
from APITrelloFramework.Helpers.Trello_Board_Request import Trello_Board
from APITrelloFramework.Helpers.Trello_List_Requests import Trello_List
import pytest


@pytest.fixture
def list_fixture():
    test_board = Trello_Board()
    new_board = test_board.Create_Board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = Trello_List()
    new_list = test_list.Create_List(board_id)
    return new_list, test_board, board_id, test_list


@pytest.mark.create_trello
def test_list_board(list_fixture):
    '''test_board = Trello_Board()
    new_board = test_board.Create_Board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = Trello_List()
    new_list = test_list.Create_List(board_id)'''
    assert list_fixture[0].status_code == 200, "List creation unsuccessful"
    res2 = list_fixture[0].json()
    list_id = res2['id']
    del_board = list_fixture[1].Del_Board(list_fixture[2])


@pytest.mark.get_trello
def test_get_list(list_fixture):
    '''test_board = Trello_Board()
    new_board = test_board.Create_Board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = Trello_List()
    get_list = test_list.Create_List(board_id)'''
    assert list_fixture[0].status_code == 200, "Fetch List unsuccessful"
    res2 = list_fixture[0].json()
    list_id = res2['id']
    del_board = list_fixture[1].Del_Board(list_fixture[2])


@pytest.mark.upd_trello
def test_update_list(list_fixture):
    '''test_board = Trello_Board()
    new_board = test_board.Create_Board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = Trello_List()
    new_list = test_list.Create_List(board_id)'''
    assert list_fixture[0].status_code == 200, "List rename unsuccessful"
    res2 = list_fixture[0].json()
    list_id = res2['id']
    query_param = namecreation.New_List_Name
    update_list = list_fixture[3].Update_List(query_param, list_id)
    assert update_list.status_code == 200, "List Deletion unsuccessful"
    del_board = list_fixture[1].Del_Board(list_fixture[2])


@pytest.mark.del_trello
def test_del_list(list_fixture):
    '''test_board = Trello_Board()
    new_board = test_board.Create_Board()
    res1 = new_board.json()
    board_id = res1['id']
    test_list = Trello_List()
    new_list = test_list.Create_List(board_id)'''
    assert list_fixture[0].status_code == 200, "List creation unsuccessful"
    res2 = list_fixture[0].json()
    list_id = res2['id']
    del_list = list_fixture[3].Del_List(list_id)
    del_board = list_fixture[1].Del_Board(list_fixture[2])
