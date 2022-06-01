import requests

endpoint = "http://localhost:8000/"

get_response = requests.post(
    endpoint, json={'title': "new new", 'content': 'New Product', "price": "abd444"})

print(get_response.json())
# print(get_response.text)
# print(get_response.status_code)
