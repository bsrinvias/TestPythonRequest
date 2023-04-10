import random
from urllib.parse import urljoin
import random
import random
uri='https://api.trello.com/1/boards/'
endpoint='1'
finalurl=urljoin(uri,endpoint)
print(finalurl)

Board='Board'
ran=random.randint(1,1000)
print(Board)
print(ran)
print(Board+str(ran))