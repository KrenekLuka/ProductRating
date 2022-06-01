import requests
from token_path import token_path


with open(f'{token_path}rating_api_token.txt') as read_file:
    token = read_file.readlines()


product_id = input("What product id do you wish to delete: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not of value 'int'")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint,  headers={
        "Authorization": f"Token {token[0]}"})
