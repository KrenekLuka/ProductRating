import requests
from getpass import getpass
from token_path import token_path


def register_user():
    auth_endpoint = "http://localhost:8000/api/register/"

    username = input('Enter your username: ')
    password = getpass('Enter your password: ')

    data = {
        "username": username,
        "password": password
    }

    auth_response = requests.post(auth_endpoint, json=data)

    print(auth_response)


register_user()
