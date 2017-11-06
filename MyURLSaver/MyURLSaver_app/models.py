from django.db import models
from django.contrib.auth.models import AbstractUser

class URL(models.Model):
    url = models.CharField(max_length=300)
    date = models.DateField()

class User(AbstractUser):
    urls = models.ManyToManyField(URL)

    def add_url(self, url_str):
        url, created = URL.objects.get_or_create(url=url_str)
        self.urls.add(url)
        self.save()




