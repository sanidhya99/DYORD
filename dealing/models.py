from django.db import models
from register.models import CustomUser

class product(models.Model):
    name=models.CharField(unique=True,max_length=50)
    price=models.IntegerField()
    benifits=models.CharField(max_length=100)

class delivery(models.Model):
    reciever=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    obj=models.ForeignKey(product,on_delete=models.CASCADE)
    address=models.CharField(max_length=500)
    number=models.IntegerField()
    delivered=models.BooleanField(default=False)
    def __str__(self):
        return f"Delivery {self.pk}"
    