from django.shortcuts import render
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions

class blogpost(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
class blogchange(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field='topic'
    def get_permissions(self):
        return [permissions.IsAdminUser()]
