from django.db import models
import requests
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
import os
from django.conf import settings
import string
from collections import defaultdict
from random import SystemRandom

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
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('mapaguapi:problems', args={self.id,})

    def save(self, *args, **kwargs):
        if not self.slug:
            rand_letters = ''.join(
                SystemRandom().choices(
                    string.ascii_letters + string.digits,
                    k=5,
                )
            )
            self.slug = slugify(f'{self.title}-{rand_letters}')

        saved = super().save(*args, **kwargs)

        return saved


    
