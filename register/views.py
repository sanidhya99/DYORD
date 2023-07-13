from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import *
from .renderers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
def get_tokens(user):
    refresh=RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }

class UserRegistration(generics.ListCreateAPIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens(user)
            return Response({'msg':'Registration Successfull','token':token})
        return Response(serializer.errors)
class UserLogin(generics.ListCreateAPIView):
    serializer_class=LoginSerializer
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if(user!=None):
                token=get_tokens(user)
                return Response({'msg':'Login Successfull','token':token})
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not valid',]}})
        return Response(serializer.errors)
class UserProfile(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    renderer_classes=[UserRenderer]
    def get(self, request, format=None):
        serializer=UserSerializer(request.user)
        return Response(serializer.data)

           
        



