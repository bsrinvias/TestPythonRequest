import pytest
@pytest.mark.smoke
def test_one():
    a=10
    b=10
    assert a==b
@pytest.mark.regression
def test_two():
    name='selenium'
    train='selenium training'
    assert name in train
@pytest.mark.smoke
def test_three():
    name='api'
    train1='api training'
    assert name in train1 ,"Name does not exist"