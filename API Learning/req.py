import requests
#import json
from requests_oauthlib import OAuth1
#from requests import OAuth1
auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
              '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988', 'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46','')
r=requests.get("https://api.trello.com/1/boards/63e38352a255adaf82ea3a97",auth=auth)

print(r.status_code)
print(r.json())
#r.status_code=200
assert r.status_code==200,"Failure"
r.raise_for_status()
print(r.text)
#json dump
