import requests, json, jsonpath
from .test_stundent2 import first

def test():
    first_obj=first()
    first_obj.test_status_code_200()

