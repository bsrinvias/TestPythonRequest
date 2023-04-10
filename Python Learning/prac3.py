from urllib.parse import urljoin
import requests


uri='https://api.trello.com/1/boards/'
Board_Name='TEST'
final_create_board_url=urljoin(uri,Board_Name)
final_get_board_url='https://api.trello.com/1/boards/'
final_Rename_board_url='https://api.trello.com/1/boards/'
final_del_board_url='https://api.trello.com/1/boards/'
print(final_create_board_url)
print(final_get_board_url)
print(final_Rename_board_url)
print(final_del_board_url)
response=requests.post(url=final_create_board_url)
