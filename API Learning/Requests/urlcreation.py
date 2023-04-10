
import posixpath
from urllib.parse import urljoin

base_url ='https://api.trello.com/1/lists?name=List'
query_param='query_param'

print(base_url)
print(query_param)
result = urljoin(base_url, query_param)

# 👇️ https://bobbyhadz.com/images/static/cat.jpg
print(result)
#https://bobbyhadz.com/images/static/cat.jpg
#https://api.trello.com/1/lists?name='list'&idBoard={{Bid}}

