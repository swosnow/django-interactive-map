from django.db import models
import requests

class Problem(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    description_is_html = models.BooleanField(default=False)
    cep = models.BigIntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    slug = models.SlugField(unique=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return self.title


    def get_lng_and_lat(self):
        pass

# Create your models here.
