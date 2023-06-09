import requests

#API endpoint
endpoint = "http://127.0.0.1:8000/api/" #Django API endpoint we use
endpoint = "http://127.0.0.1:8000/api/ModelData"
endpoint = "http://127.0.0.1:8000/api/APIView"
endpoint = "http://127.0.0.1:8000/api/PostView"

'''
response = requests.get(endpoint, params={"Param" : 123}, json={"Gael" : "Power!"})
print(response.json())
''' 
#This gets data from our backend through get request

#API -> HTTP Request, this is basically our HTTP request
#form argument for form data, json argument for JSON data that we are sending

# We passed JSON data as request data, and it echoed back to us in response below 

'''#print(response.text) #printing raw text source code response
#print(response.status_code) #printing JSON response of HTTP request''' 



'''
HTTP request -> source code text of html
REST API HTTP Request -> JSON something that our code can use -> almost structured as a python dictionary 
'''

get_response = requests.post(endpoint, json={'title':'Hello world'}) 
print(get_response.json())