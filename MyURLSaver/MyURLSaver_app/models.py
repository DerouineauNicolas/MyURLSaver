from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class URL(models.Model):
    url_name = models.CharField(max_length=300)
    date = models.DateField()

class User(AbstractUser):
    urls = models.ManyToManyField(URL)

    def add_url(self, url_str):
        url, created = URL.objects.get_or_create(url_name=url_str,date=datetime.now())
        self.urls.add(url)
        self.save()

    def del_url(self, url_str):
        #print(url_str)
        url, created = URL.objects.get_or_create(url_name=url_str)
        self.urls.remove(url)
        self.save()




