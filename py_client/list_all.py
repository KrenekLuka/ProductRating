import requests

luka_token = "041b52477ff11c06e095259387faa92636c6b963"


endpoint = "http://localhost:8000/api/products/"
get_response = requests.get(endpoint, headers={
    "Authorization": f"Token {luka_token}"})
data = get_response.json()
print("Page 1 \n")
print(data['results'], '\n')

next_endpoint = data['next']
page = 2
while next_endpoint is not None:
    print(f"Page {page} \n")
    get_response = requests.get(next_endpoint, headers={
        "Authorization": f"Token {luka_token}"})
    next_data = get_response.json()
    print(next_data['results'])
    next_endpoint = next_data['next']
    page += 1
