from django.contrib import admin
from .models import Album
from django import forms
# Register your models here.


class AlbumsModelForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'release_datetime', 'cost', 'approved']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['approved'].help_text = 'Approve the album if its name is not explicit'


class AlbumModelAdmin(admin.ModelAdmin):
    readonly_fields = ['creation_datetime']
    list_display = ('name', 'artist', 'creation_datetime', 'release_datetime', 'cost', 'approved')


admin.site.register(Album, AlbumModelAdmin, form=AlbumsModelForm)
