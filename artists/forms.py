from django import forms
from . import models


class CreateArtistForm(forms.ModelForm):
    class Meta:
        model = models.Artist
        fields = ['Stage_name', 'Social_link']
