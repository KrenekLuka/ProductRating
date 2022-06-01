import requests
from token_path import token_path


with open(f'{token_path}rating_api_token.txt') as read_file:
    token = read_file.readlines()

endpoint = "http://localhost:8000/api/products/"


list_data = [
    {"name": "Apple", "price": 1.50, },
    {"name": "Pear", "price": 0.89},
    {"name": "Orange", "price": 1.02},
    {"name": "Kiwi", "price": 1.40},
    {"name": "Lemon", "price": 1.22},
    {"name": "Bannana", "price": 1.02},
    {"name": "Blueberry", "price": 2.20},
    {"name": "Peach", "price": 2.20},
    {"name": "Watermellon", "price": 4.40},
    {"name": "Strawberry", "price": 3.42},
    {"name": "Fig", "price": 0.22},
    {"name": "Plum", "price": 0.30},
    {"name": "Rosehip", "price": 0.60},
    {"name": "Grape", "price": 0.25},
    {"name": "Mellon", "price": 3.40},
    {"name": "Mango", "price": 2.20},
    {"name": "Papaya", "price": 1.38},
    {"name": "Passionfruit", "price": 1.48},
    {"name": "Cherry", "price": 0.05},
    {"name": "Coconut", "price": 3.20}
]

for item in list_data:
    get_response = requests.post(endpoint, json=item, headers={
        "Authorization": f"Token {token[0]}"})

    print(get_response.json())
