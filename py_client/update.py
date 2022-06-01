import requests
from token_path import token_path


with open(f'{token_path}rating_api_token.txt') as read_file:
    token = read_file.readlines()


product_key = input("Input product number to update: ")
endpoint = f"http://localhost:8000/api/products/{product_key}/update/"

data = {
    "name": "Product renamed",
    "price": 1.05
}

get_response = requests.put(endpoint, json=data, headers={
    "Authorization": f"Token {token[0]}"})
print(get_response.json())
