import requests,json
from pprint import pprint
requests_uri='http://api.openweathermap.org/data/2.5/weather?lat=17.3753&lon=78.4744&appid=1a4b8830a8ed4792b00a7ec04cd4481c'
res=requests.post(requests_uri)
res_data=res.json()
print("Name of the City:",res_data['name'])
assert res_data['name']=='Hyderabad','AssertionError'
print("Name of the Country:",res_data['sys']['country'])
assert res_data['sys']['country']=='IN','AssertionError'
print("Temparature min:",res_data['main']['temp_min'])
if res_data['main']['temp_min']>0:
    print("Min Temparature is greater than 0")
else:
    print("Min Temparature is not avaialbe")
print("Temparature:",res_data['main']['temp'])
if res_data['main']['temp']>0:
    print("Temparature is greater than 0")
else:
    print("Temparature is not avaialbe")


