import pytest
@pytest.fixture()
def setup():
    print("start")
    yield
    print("end")
def test_createList(setup):
    print("List Created Sucessfully")
def test_ViewList(setup):
    print("List Viewed Sucessfully")
def test_RenameList(setup):
    print("List Renamed Sucessfully")
def test_DeleteList(setup):
    print("List Deleted Sucessfully")