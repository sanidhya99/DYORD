from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['name','price','benifits']
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model=delivery
        fields=['reciever','address','number']        
 