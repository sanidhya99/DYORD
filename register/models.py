from django.db import models
from .manage import *
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=20)
    number=models.IntegerField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects=CustomUserManager()
    REQUIRED_FIELDS=["name","number"]
    USERNAME_FIELD='email'
    def __str__(self):
        return self.email


    
