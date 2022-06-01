import requests
from getpass import getpass
from token_path import token_path


def get_authentication_token():
    auth_endpoint = "http://localhost:8000/api/auth/"

    username = input('Enter your username: ')
    password = getpass('Enter your password: ')

    data = {
        "username": username,
        "password": password
    }

    auth_response = requests.post(auth_endpoint, json=data)

    if auth_response.status_code == 200:
        token = auth_response.json()['token']
        print(token)
        with open(f"{token_path}rating_api_token.txt", "wt") as text_file:
            text_file.write(token)
            text_file.close()
    return None


get_authentication_token()
