from datetime import datetime
from django.db import models
from artists.models import Artist
from django.core.validators import FileExtensionValidator
from model_utils.models import TimeStampedModel
from imagekit.models import ProcessedImageField


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

class Song(models.Model):

    name = models.CharField(verbose_name="name",max_length=100,blank=True,null=False)
    image = models.ImageField(upload_to='images/')
    thumb = ProcessedImageField(upload_to = 'thumbs/' , format='JPEG')
    audio = models.FileField(upload_to = 'audio/', validators=[FileExtensionValidator( allowed_extensions=['mp3', 'wav'] ) ])
    album = models.ForeignKey(Album,on_delete=models.CASCADE , default=None)

    def __str__(self):
        return self.name
