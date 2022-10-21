from django import forms
from . import models

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = ['name' ,'release_datetime','cost','artist','approved']
        widgets = {
            'release_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
