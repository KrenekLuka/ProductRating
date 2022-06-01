import requests

luka_token = "041b52477ff11c06e095259387faa92636c6b963"


product_id = input("What product id do you wish to delete: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not of value 'int'")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint,  headers={
        "Authorization": f"Token {luka_token}"})

# print(get_response.status_code, get_response.status_code == 204)
