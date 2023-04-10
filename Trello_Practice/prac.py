#https://www.google.com/search?q=API+Automation+using+python+youtube&rlz=1C1GCEU_enIN941IN941&oq=API+Automation+using+python+youtube&aqs=chrome..69i57j0i546l2j69i64.16608j0j7&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:a84020bb,vid:itrgje2oqqU
import json
import jsonpath
import requests
#import json
from requests_oauthlib import OAuth1
#from requests import OAuth1
from pprint import pprint
auth = OAuth1('e8a0e2dd807820e641f0960bd3821077',
              '76fe7656dd78fa845cbb7e1cfa745ce56d032bc3369c8609aff47304ba20a988', 'ATTA7ae54d5f4cf39c3ba90e74bd88a236e19474d4c7499ada475976547ac2102c7657832A46','')
res=requests.get("https://api.trello.com/1/boards/63e38352a255adaf82ea3a97",auth=auth)
print(res.status_code)
res1=json.loads(res.text)
id=res1['id']
print(res.json())
print(id)

