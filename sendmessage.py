import requests
from settings import TOKEN


BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
ID="6256447055"
params = {
    'chat_id':{ID},
    'text': 'Qanday'
}

sendmessage_url = f'{BASE_URL}/sendMessage'
response = requests.get(sendmessage_url, params=params)
