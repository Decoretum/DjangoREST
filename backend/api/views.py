from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
def home(request, *args, **kwargs):
    body = request.body #byte string of JSON Data in the request
    print(request.GET) #fetch URL query parameters from request
    try:
        data = json.loads(body) #basically turns string of JSON Data into a Python dictionary/hashmap
    except:
        print('error')

    # data['headers'] = request.headers # request.META 
    data['Purpose'] = "Backend Practice"
    data['content_type'] = request.content_type
    data['headers'] = dict(request.headers) #since HTTP headers are not JSON serializeable, we make them into Python dict
    return JsonResponse(data)
    '''
    When this function is run, we send out a JSON response with params and JSON data to be sent from
    basic.py, and we return the JSON response from this function that has been manipulated
    '''

def modelData(request):
    requestdata = json.loads(request.body)
    model_data = Product.objects.all().order_by('?').first()
    data = {}

    '''if modelData:
        data['PK'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price'''
    
    if model_data:
        data = model_to_dict(model_data) #we transform model instance to dict instantly
        data = model_to_dict(model_data, fields=['title','content']) #we can specify what model fields API will respond with
        data['requestData'] = requestdata #we integrated request data to actual JSON response
    return JsonResponse(data) #JSON response containing model data
    '''
    Serialization - we create a model instance, turn it into a Python Dict, 
    send it as a JSON response to client
    '''

@api_view(['GET']) #Django rest framework already doing the GET Request for you in view
def APIView(request):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        #hashmap = model_to_dict(model_data)
        data = ProductSerializer(instance).data #also does model_to_dict(model_data)
        '''
        Using Serializer, we automated model functions and returning the model's data
        '''
    return Response(data) #JSON data

 
#Django rest framework already doing the POST Request for you in view
#Ingests data from POST request
#Used to create an object instance using serializers
@api_view(['POST']) 
def PostView(request):
    serializer = ProductSerializer(data=request.data)
    ''' Checks if data being POST by request matches how data is formatted in serializer '''
    if serializer.is_valid(raise_exception=True): #Raise exception used for data validation when passed to serializers
        instance = serializer.save() 
        #Basically saves Model data using serializer based from model fields' parameters
        #It's like creating a new object hahah actually it is a new objet
        print(instance)
    return Response(serializer.data) #JSON data
