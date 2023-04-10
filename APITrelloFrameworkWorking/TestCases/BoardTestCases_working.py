import pytest
import logging
import allure
import allure_pytest

import Trello_Practice.test_CreateList
from APITrelloFramework.Helpers.Trello_Board_Request import test_Trello
from APITrelloFramework.Helpers.Trello_List_Requests_before import test_List_Trello
from APITrelloFramework.Configuration import namecreation


'''def test_create_board():
    test_board = test_Trello()
    new_board,response = test_board.test_create_board()
    print(response.status_code)
    assert response.status_code == 200, "Board creation unsuccessful"
    #test_board.test_del_board(new_board['id'])'''


def test_create_board():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    assert new_board.status_code == 200, "Board creation unsuccessful"
    res1 = new_board.json()
    test_board.test_del_board(res1['id'])

def test_get_board():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1 = new_board.json()
    board_id = res1['id']
    get_board = test_board.test_get_board(board_id)
    assert get_board.status_code == 200, "Fetch board unsuccessful"
    test_board.test_del_board(res1['id'])

def test_update_board():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1=new_board.json()
    board_id = res1['id']
    query_param=namecreation.New_Board_Name
    update_board = test_board.test_update_board(query_param,board_id)
    assert update_board.status_code == 200, "Update board unsuccessful"
    test_board.test_del_board(res1['id'])

def test_delete_board():
    test_board = test_Trello()
    new_board = test_board.test_create_board()
    res1 = new_board.json()
    board_id = res1['id']
    del_board=test_board.test_del_board(board_id)
    assert del_board.status_code==200,"Board Deletion unsuccessful"













