import requests

endpoint = 'http://localhost:8000/api/products/ProductList'

data = {
    'title' : 'Sex',
    'content' : 'Pizza HAHAHAAH',
    'price' : 24.21
}
response = requests.get(endpoint, json=data)
print(response.json())