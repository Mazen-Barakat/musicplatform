from email.policy import default
from datetime import datetime
from unicodedata import decimal, name
from django.db import models
from artists.models import Artist
# Create your models here.


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(default='New Album', max_length=150, blank=True)
    creation_datetime = models.DateTimeField(default=datetime.now)
    release_datetime = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=False)

    def __str__(self):
        return self.name
