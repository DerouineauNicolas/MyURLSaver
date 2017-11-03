from django.db import models
from django.contrib.auth.models import AbstractUser

class URL(models.Model):
    url = models.CharField(max_length=300)
    date = models.DateField()

class User(AbstractUser):
    url = models.ManyToManyField(URL)




