import requests

endpoint = 'http://localhost:8000/api/products/UpdateProduct/24/'
data = {
    'title' : 'Hello darkness mga bobo',
    'content' : "Oh lala"
}

response = requests.put(endpoint, json=data)
print(response.json())