import requests

endpoint = 'http://localhost:8000/api/products/DeleteView/24/'

response = requests.delete(endpoint)
print(response.status_code)