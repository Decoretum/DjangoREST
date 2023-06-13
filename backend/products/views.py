from rest_framework import generics, mixins, viewsets, permissions, authentication
from .models import Product
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .permissions import *

''' 
Class-based views 
API Views automatically return a response of the data that could be transmitted to JSON for front-end
'''

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


'''
This is a PUT function since we are updating
'''
class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    #Specify the look_up field for this Viewset

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title 
        print(instance.title)


class ProductDeleteAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'

    def perform_delete(self, instance):
        super().perform_destroy(instance)

'''
This is an alternate ViewSet that is a ONE FOR ALL functionality for 
getting a model object, listing, and creating
'''
@api_view(['GET','POST'])
def AltProductView(request, pk=None):
    method = request.method
    if method == 'GET':
        if pk is not None:
            obj = Product.objects.filter(pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        #Getting one model object

        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)
        #Getting a list of model objects

    elif method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Invalid Data', status=404)
        #Creating a model object


'''
Better Version of Alt Product View using MixInView
Integrates different viewset functionalities in 1 class
'''
class ProductMixinView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #this matters for retrieving
    permission_classes = [
        #permissions.DjangoModelPermissions,
        IsStaff
        ]
    '''
    Permissions for a certain viewset are dependent on Django's User permissions 
    Post request require 'add' permission from user
    Put and Patch requests require 'change' permission from user
    delete request requires 'delete' permission from user

    Permissions are SEQUENTIAL
    '''

    authentication_classes = [authentication.SessionAuthentication]
    '''
    permissions.action
    isauthenticated proves if user that made the request has permissions
    isauthenticatedorreadonly allows user that isnt authenticated to do get but not post
    '''

    '''Create Object'''
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    '''get List or Object'''
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(args ,kwargs)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request)
    
    '''update object'''
    def put(self, request, *args, **kwargs):
        print(args, kwargs)
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, *kwargs)
    

'''
viewset.Model
'''

# class ProductRound(viewsets.ModelViewSet):

#     def list(self, request, *args, **kwargs):
#         queryset = Product.objects.all()
#         serializer_class = ProductSerializer(queryset, many=True)
#         return Response(serializer_class.data)
    
#     def retrieve(self, request, pk, *args, **kwargs):
#         print(request)
#         queryset = Product.objects.all()
#         accobj = get_object_or_404(queryset, pk=pk)
#         serializer_class = ProductSerializer(accobj, many=False)
#         return Response(serializer_class.data)
