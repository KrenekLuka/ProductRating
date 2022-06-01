import requests


luka_token = "041b52477ff11c06e095259387faa92636c6b963"


product_key = input("Input product number to update: ")
endpoint = f"http://localhost:8000/api/products/{product_key}/update/"
data = {
    "name": "Appleeeees",
    "price": 1.05
}
get_response = requests.put(endpoint, json=data, headers={
    "Authorization": f"Token {luka_token}"})
print(get_response.json())
