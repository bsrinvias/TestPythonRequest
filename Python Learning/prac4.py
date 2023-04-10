import posixpath
from urllib.parse import urljoin

base_url =r'https://api.trello.com/1/lists?name=List'
query_param='query_param'

'''path_1 = "name='list'"
path_2 = 'idBoard=Bid'


path = posixpath.join(path_1, path_2)
print(path)  # 👉️ 'images/static/cat.jpg'''

result = urljoin(base_url, query_param)

# 👇️ https://bobbyhadz.com/images/static/cat.jpg
print(result)
#https://bobbyhadz.com/images/static/cat.jpg
#https://api.trello.com/1/lists?name='list'&idBoard={{Bid}}

