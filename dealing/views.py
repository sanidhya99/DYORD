from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions

class productpost(generics.ListCreateAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
class productchange(generics.RetrieveUpdateDestroyAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='name'
    def get_permissions(self):
        return [permissions.IsAdminUser()]
    

class DeliveryListCreateView(generics.ListCreateAPIView):
    serializer_class = DeliverySerializer
    queryset = delivery.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return delivery.objects.all()
        else:
            return delivery.objects.filter(reciever=user)

    def perform_create(self, serializer):
        serializer.save(reciever=self.request.user)    

# class DeliveryUD(generics.DestroyAPIView):
#     serializer_class=DeliverySerializer
#     queryset=delivery.objects.all()
#     lookup_field='reciever_id'
#     def perform_destroy(self, instance):
#         if (self.request.user).is_superuser:
#             instance.delete()
#         elif instance.reciever==self.request.user:
#             instance.delete()
#         else:
#             return response({"error":"You are not allowed to do this"})   