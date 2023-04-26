from django.db import models
from django.contrib.auth.models import User


class UrlShort(models.Model):
    url = models.URLField()
    slug = models.CharField(max_length=10, unique=True)
    shorted_url = models.URLField()
    title = models.CharField(max_length=255)
