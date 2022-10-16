from django.db import models

# Create your models here.


class Artist(models.Model):
    Stage_name = models.CharField(max_length=100, blank=False, unique=True)
    Social_link = models.URLField(max_length=150, blank=True, null=False)

    def __str__(self):
        return self.Stage_name

    class Meta:
        ordering = ['Stage_name']
