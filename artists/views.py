from django.shortcuts import render
from albums.models import Album
from . import forms


# Create your views here.

def create_view(request):
    if request.method == 'POST':
        form = forms.CreateArtistForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CreateArtistForm()
    return render(request, 'artists/create.html', {'form': form})


def list_view(request):
    q = Album.objects.select_related('artist').all()
    artists_set = set()
    for album in q:
        artists_set.add(album.artist)

    artist_to_albums = []
    for artist in artists_set:
        temp = []
        for album in q:
            if album.artist.Stage_name == artist.Stage_name:
                temp.append(album)
        artist.albums = temp
        artist_to_albums.append(artist)

    return render(request, 'artists/list.html', {'data': artist_to_albums})
