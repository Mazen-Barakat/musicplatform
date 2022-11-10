from django.contrib import admin
from .models import Album, Song
from .forms import AlbumForm

# Register your models here.

class SongInline(admin.TabularInline):
    model = Song
    extra = 1
class AlbumModelAdmin(admin.ModelAdmin):
    form=AlbumForm
    readonly_fields = ['creation_datetime']
    list_display = ('name', 'artist', 'creation_datetime','release_datetime', 'cost', 'approved')
    inlines = [SongInline]
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)



class SongAdmin(admin.ModelAdmin):
    fields = ['name', 'album', 'image', 'image_thumbnail', 'audio']

admin.site.register(Album, AlbumModelAdmin)
admin.site.register(Song)
