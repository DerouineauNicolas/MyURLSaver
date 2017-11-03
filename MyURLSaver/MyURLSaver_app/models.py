from django.db import models
from django.contrib.auth.models import User

class URL(models.Model):
    url = models.CharField(max_length=300)
    date = models.DateField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    URLs = models.ManyToManyField(URL)



