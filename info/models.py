from django.db import models


class Blog(models.Model):
    topic = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
