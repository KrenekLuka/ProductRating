import requests

staff_token = "052716ebb157dd5b4f11daa3eeca22c3fb8e07cf"
luka_token = "7c200df578ceacccd2cf929f169cd22429bf5c34"

endpoint = "http://localhost:8000/api/products/rating/"

data = {
    "product_id": 3,
    "rating": 5
}
get_response = requests.post(endpoint, json=data, headers={
    "Authorization": f"Token {luka_token}"})
print(get_response.status_code)

print(get_response.json())
