from APITrelloFramework.Helpers.Trello_Board_Request import Trello_Board
from APITrelloFramework.Configuration import namecreation
import pytest


@pytest.fixture
def board_fixture():
    test_board = Trello_Board()
    new_board = test_board.Create_Board()
    return new_board, test_board


def test_create_board(board_fixture):
    # test_board = Trello_Board()
    # new_board = test_board.Create_Board()
    assert board_fixture[0].status_code == 200, "Board creation unsuccessful"
    res1 = board_fixture[0].json()
    board_id = res1['id']
    board_name = res1['name']
    assert board_fixture[0].headers['Content-Type'] == "application/json; charset=utf-8"
    assert board_name == namecreation.Board_name
    del_board = board_fixture[1].Del_Board(board_id)


@pytest.mark.get_trello
def test_get_board(board_fixture):
    #test_board = Trello_Board()
    #new_board = test_board.Create_Board()
    res1 = board_fixture[0].json()
    board_id = res1['id']
    get_board = board_fixture[1].Get_Board(board_id)
    assert get_board.status_code == 200, "Fetch board unsuccessful"
    del_board = board_fixture[1].Del_Board(board_id)


@pytest.mark.upd_trello
def test_update_board(board_fixture):
    #test_board = Trello_Board()
    #new_board = test_board.Create_Board()
    res1 = board_fixture[0].json()
    board_id = res1['id']
    query_param = namecreation.New_Board_Name
    update_board = board_fixture[1].Update_Board(query_param, board_id)
    assert update_board.status_code == 200, "Update board unsuccessful"
    board_fixture[1].Del_Board(res1['id'])
    del_board = board_fixture[1].Del_Board(board_id)


@pytest.mark.del_trello
def test_delete_board(board_fixture):
    #test_board = Trello_Board()
    #new_board = board_fixture[0].Create_Board()
    res1 = board_fixture[0].json()
    board_id = res1['id']
    del_board = board_fixture[1].Del_Board(board_id)
    assert del_board.status_code == 200, "Board Deletion unsuccessful"
