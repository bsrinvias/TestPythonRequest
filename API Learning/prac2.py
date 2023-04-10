#1a4b8830a8ed4792b00a7ec04cd4481c
import requests,json,pprint
from pprint import pprint
requests_uri='http://api.openweathermap.org/data/2.5/weather?lat=17.3753&lon=78.4744&key=1a4b8830a8ed4792b00a7ec04cd4481c'
#requests_key='1a4b8830a8ed4792b00a7ec04cd4481c'
#baseurl=requests_uri+"&appid="+requests_key
#print(baseurl)
res=requests.post(requests_uri)
res_data=res.json()
#pprint(res_data)
print("Name of the City:",res_data['name'])
assert res_data['name']=='Hyderabad','AssertionError'
print("Name of the Country:",res_data['sys']['country'])
assert res_data['sys']['country']=='IN','AssertionError'
print("Temparature min:",res_data['main']['temp_min'])
print("Temparature:",res_data['main']['temp'])


