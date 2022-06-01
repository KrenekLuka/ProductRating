import requests

luka_token = "041b52477ff11c06e095259387faa92636c6b963"


endpoint = "http://localhost:8000/api/products/"
get_response = requests.get(endpoint, headers={
    "Authorization": f"Token {luka_token}"})
print(get_response.json())
