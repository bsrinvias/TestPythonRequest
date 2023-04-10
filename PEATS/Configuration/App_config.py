import os
#https://medium.com/geekculture/how-to-hide-passwords-and-secret-keys-in-your-python-scripts-a8904d5560ec
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
print(username)
print(password)




API_HOSTS = {
    "test": "https://api.trello.com/1/boards/?name=TEST",
    "dev": "",
    "prod": ""
}