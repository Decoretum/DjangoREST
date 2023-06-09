from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price', #reference to property/function of Product model
            'Advertise',
            'Greet',
        ]