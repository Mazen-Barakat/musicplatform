from django.contrib import admin
from .models import Album, Song
from .forms import AlbumForm
from .validator import validate_form

# Register your models here.

class SongInline(admin.TabularInline):
    model = Song
    min_num = 1
    extra = 0


class SongAdmin(admin.ModelAdmin):
    fields = ['name', 'album', 'image', 'image_thumbnail', 'audio']


class AlbumModelAdmin(admin.ModelAdmin):
    
    form=AlbumForm
    readonly_fields = ['creation_datetime']
    list_display = ('name', 'artist', 'creation_datetime','release_datetime', 'cost', 'approved')
    inlines = [SongInline]

    def save_model(self, request, obj, form, change):
        validate_form(self, obj)
        super().save_model(request, obj, form, change)


    def album_songs(self, Album):
        return Album.songs.count()


admin.site.register(Album, AlbumModelAdmin)
admin.site.register(Song)
