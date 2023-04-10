import requests,json,pprint
requests_uri='http://api.openweathermap.org/data/2.5/weather?q='
city=input("Enter City Name: ")
requests_key='1a4b8830a8ed4792b00a7ec04cd4481c'
baseurl=requests_uri+city+"&appid="+requests_key
print(baseurl)
res=requests.get(baseurl)
res_data=res.json()
print(res_data)
print("longitude: ",res_data['coord']['lon'])
print("latitude: ",res_data['coord']['lat'])