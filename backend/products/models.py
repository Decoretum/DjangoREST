from django.db import models
from decimal import Decimal

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def Advertise(self):
        try:
            return self.title + ": " + self.content
        except:
            return None

    def Greet(self):
        try:
            return "Hi!! Gael here!" #with a serializer, if this is None in the request, then serializer will return None
        except:
            return None