import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title' : 'Love',
    'content' : 'You are my one',
    'price' : 24.21
}
response = requests.post(endpoint, json=data)
print(response.json())