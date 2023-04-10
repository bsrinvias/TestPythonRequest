import pytest

#decorator
@pytest.mark.smoke
def test_login():
     print("Login successful")

@pytest.mark.regression
def test_addproduct():
    print("addproduct successful")

@pytest.mark.smoke
def test_logout():
     print("Logout successful")