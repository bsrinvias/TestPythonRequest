import pytest

@pytest.fixture
def create_board():
    test_board = Trello_Board()
    new_board = test_board.Create_Board()
