import requests
from getpass import getpass


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
        # return {"Authorization": f"Token {token}"}
        print(token)
    return None


get_authentication_token()
