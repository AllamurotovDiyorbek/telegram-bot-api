import requests
from settings import TOKEN


BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
ID=""
params = {
    'chat_id':{ID},
    'text': 'Nima gap'
}

sendmessage_url = f'{BASE_URL}/sendMessage'
response = requests.get(sendmessage_url, params=params)
