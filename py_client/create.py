import requests

from token_path import token_path


with open(f'{token_path}rating_api_token.txt') as read_file:
    token = read_file.readlines()

endpoint = "http://localhost:8000/api/products/"

data = {
    "name": "Lamp",
    "price": 12.21,
}
get_response = requests.post(endpoint, json=data, headers={
    "Authorization": f"Token {token[0]}"})

print(get_response.json())
