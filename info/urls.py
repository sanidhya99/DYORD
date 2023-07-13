from .views import *
from django.urls import path

urlpatterns=[
    path("blogs/" ,blogpost.as_view(),name="Create-List-blogs"),
    path("blogs/<str:topic>/" ,blogchange.as_view(),name="Modify-blogs"),
    

           ]