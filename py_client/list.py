import requests
from token_path import token_path


with open(f'{token_path}rating_api_token.txt') as read_file:
    token = read_file.readlines()

endpoint = "http://localhost:8000/api/products/"

get_response = requests.get(endpoint, headers={
    "Authorization": f"Token {token[0]}"})
print(get_response.json())
