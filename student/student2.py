import testcon

# check that status code is 200
def test_status_code_200():
    assert testcon.response.status_code == 200
def test_header_content():
    assert testcon.student2.response.headers['Content-Type'] == "application/json; charset=utf-8"
def test_name_content():
    assert "name" in testcon.student2.response_body
def test_name_one():
    assert testcon.student2.response_body['name'] == 'Leanne Graham'
def test_name_one():
    assert testcon.student2.response_body['company']['name'] == 'Romaguera-Crona'

if __name__ == '__main__':
    test.main()






