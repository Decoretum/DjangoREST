from rest_framework import generics
from .models import Product
from .serializers import *

''' Class-based views '''

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    
    '''We then serialize data from POST Request'''
    serializer_class = ProductSerializer

    '''look-up field, which field we want to lookup on this queryset (for ex. pk, or a specific value)'''
    ''' look-up field: pk '''

'''
CreateAPI View is used to "Create" a model object
ListAPI View is used to "List" all model objects
Combining them is good since ListAPI View only needs queryset and serializer and won't touch the 
    perform_create function that's intended for CreateAPI View

'''
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    ''' 
    function below is automatically executed by the API Class of CreateAPIView 
    serializer below is serializer_class specified
    '''
    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        price = serializer.validated_data.get('price')

        if content == None:
            content = title
        
        if title == 'Sex':
            title = 'A Censored Title'

        ''' 
        validated data here come from the request data that was validated to the serializer 
        Serializer save is used to SPECIFY how we save the created model object
        '''
        print(serializer.validated_data)
        serializer.save(content = content, title = title)
        


