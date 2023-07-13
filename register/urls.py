from .views import *

from django.urls import path

urlpatterns=[
    path("register/" ,UserRegistration.as_view(),name="UserCreation"),
    path("login/" ,UserLogin.as_view(),name="UserAuth"),
    path("profile/" ,UserProfile.as_view(),name="UserProfile"),
            ]