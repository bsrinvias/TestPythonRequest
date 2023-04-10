import pytest
def test_createCard():
    print("Card Created Sucessfully")
@pytest.mark.skip
def test_ViewCard():
    print("Card Viewed Sucessfully")
@pytest.mark.xpass
def test_RenameCard():
    print("Card Renamed Sucessfully")
@pytest.mark.xfail
def test_DeleteCard():
    print("Card Deleted Sucessfully")