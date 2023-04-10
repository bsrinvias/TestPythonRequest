import requests
class CRUD_Operations:
    def __init__(self, url, params, auth):
        self.url =url
        self.params = params
        self.auth =auth
    def test_create(self):
        response = requests.post(self.url, params=self.params, auth=self.auth)
        res1 = response.json()
        get_Board_id = res1['id']
        print(res1)
        return get_Board_id, self.auth
    def test_get(self):
        get_Board_id, auth = self.test_create()
        get_board = requests.get(self.url + get_Board_id, auth=self.auth)
        assert get_board.status_code == 200, "Get Board Response code is incorrect"
    def test_update_board(self):
        get_Board_id, auth = self.test_create()
        query_param = 'name=TESTtest3'
        upd_board = requests.put(self.url + get_Board_id, params=query_param, auth=self.auth)
        print(upd_board.url)
        assert upd_board.status_code == 200, "Update Board Response code is incorrect"
    def test_del_board(self):
        get_Board_id, auth = self.test_create()
        del_board = requests.delete(self.url + get_Board_id, auth=self.auth)
        assert del_board.status_code == 200, "Delete Board Response code is incorrect"