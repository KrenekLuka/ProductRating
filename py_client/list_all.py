import requests
from token_path import token_path


with open(f'{token_path}rating_api_token.txt') as read_file:
    token = read_file.readlines()


endpoint = "http://localhost:8000/api/products/"
get_response = requests.get(endpoint, headers={
    "Authorization": f"Token {token[0]}"})

data = get_response.json()

print("Page 1 \n")
print(data['results'], '\n')

next_endpoint = data['next']

page = 2
while next_endpoint is not None:
    print(f"Page {page} \n")

    get_response = requests.get(next_endpoint, headers={
        "Authorization": f"Token {token[0]}"})

    next_data = get_response.json()

    print(next_data['results'])

    next_endpoint = next_data['next']
    page += 1
