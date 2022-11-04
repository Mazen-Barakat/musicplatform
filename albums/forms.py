from django import forms
from . import models
from .validator import validate_form

class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = ['name', 'artist', 'release_datetime', 'cost', 'approved']
        validators = [validate_form]
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['approved'].help_text = 'Approve the album if its name is not explicit'
