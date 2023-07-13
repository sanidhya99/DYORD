from .views import *
from django.urls import path

urlpatterns=[
    #url to create and list blog 
    path("blogs/" ,blogpost.as_view(),name="Create-List-blogs"),
    #url to change or delete blog
    path("blogs/<str:topic>/" ,blogchange.as_view(),name="Modify-blogs"),
    

           ]
