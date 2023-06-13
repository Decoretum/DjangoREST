from rest_framework import serializers
from .models import Product

'''
Serializers allow us to ADD MODIFICATIONS to a returned model attribute or method
We can have multiple serializers for different or one model
Can also ingest and clean data to validate data
'''

class ProductSerializer(serializers.ModelSerializer):

    #Initializing serializing methods
    get_discount = serializers.SerializerMethodField(read_only = True)
    NoInstanceMethod = serializers.SerializerMethodField(read_only = True)

    ''' 
    We define a serializer attribute or method in order to serialize a certain field from model by adding
    on top of model's original method

    Using serializer attribute or method, we can DIRECTLY access model attributes and methods

    We transform JSON data into python data (dictionary) that could be transmitted to somewhere as JSON or Python data
    '''
    def get_get_discount(self,obj):
        if hasattr(obj,'id'):                   
            return obj.get_discount() + 100
        else:
            return 'NO DISCOUNT'
        
        '''
        In this case, 'obj' could be a valid Model OBJECT, or it could be an ORDERED DICTIONARY
        We use if and else, because 'else' occurs when there IS NO OBJECT INSTANTIATED or NO MODEL ID
        If no object instantiated, then you can't call obj.get_discount()
        hasattr(a, b) can also be isinstance(a,b)
        '''
    
    def get_NoInstanceMethod(self, obj):
        print(obj)
        return 'Data for non-objects!'
 
        '''
        example of a serializer method that does not need any object instantiation
        "obj" here is simply an ordered dictionary containing key-value data
        '''

    class Meta:
        model = Product

        '''
        Fields can be instance methods or properties from models
        reference to property/function of Product model
        Fields that are blank = True / null = True will default be added to data, whether 
        MODEL OBJECT OR ORDERED DICTIONARY DATA
        '''
        
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price', 
            'Advertise',
            'Greet',
            'get_discount', #from serializer's method
            'NoInstanceMethod' #from serializer's method as well
        ]

class SecondProductSerializer(serializers.ModelSerializer):
    random = serializers.SerializerMethodField(read_only = True)
    def get_random (self,obj):
        return 'Random STUFF'
    
    '''
    In this example, we only returned a 'random' field from the serializer
    '''

    
    class Meta:
        model = Product
        fields = (
            'random',
        )

    
