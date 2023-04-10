def test_1():
    x=10
    y=10
    assert x==y
def test_2():
    name='Selenium'
    title='Selenium web automation'
    assert name in title

def test_3():
    name = 'Jenkins'
    title = 'Jenkins web automation'
    assert name in title ,"Jenkins does not exist"