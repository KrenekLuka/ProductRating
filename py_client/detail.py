import requests

from auth import get_authentication_token


headers = get_authentication_token()

if headers:
    product_key = input("Input product number to view: ")
    endpoint = f"http://localhost:8000/api/products/{product_key}/"

    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())
