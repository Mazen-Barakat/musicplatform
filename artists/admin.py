from django.contrib import admin
from .models import Artist

# Register your models here.


class ArtistModelAdmin(admin.ModelAdmin):
    def number_of_approved_albums(self, Artist):
        return Artist.album_set.filter(approved=True).count()

    list_display = ('Stage_name', 'Social_link', 'number_of_approved_albums')


admin.site.register(Artist, ArtistModelAdmin)
