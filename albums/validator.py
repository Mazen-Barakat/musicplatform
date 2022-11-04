import rest_framework.exceptions 
from django.forms import ValidationError 


def validate_serializer(self):
    if self.songs.count() < 1:
        raise rest_framework.exceptions.ValidationError('Album must have at least one song')
    
def validate_form(self, obj):
    if obj.songs.count() < 1:
        raise ValidationError('Album must have at least one song')