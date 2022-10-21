from datetime import datetime
from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel


# Create your models here.


class Album(TimeStampedModel):
    name = models.CharField(default='New Album', max_length=150, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField(default=datetime.now)
    release_datetime = models.DateTimeField(blank=False, null=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
