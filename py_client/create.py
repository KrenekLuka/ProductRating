import requests

# from auth import get_authentication_token


# headers = get_authentication_token()

# if headers:
token = "18df89ed39251d49ca145d35e91e9b82f107ad63"
endpoint = "http://localhost:8000/api/products/"

data = {
    "name": "Light-Beer",
    "price": 8.99,
}
get_response = requests.post(endpoint, json=data, headers={
    "Authorization": f"Token {token}"})
print(get_response.json())
