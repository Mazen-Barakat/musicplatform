from django.shortcuts import render
from albums.models import Album
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from . import forms


# Create your views here.

@method_decorator(login_required, name='dispatch')
class create_view(View):
    form_class = forms.CreateArtistForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'artists/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'artists/create.html', {'form': form})


class list_view(View):

    def get(self, request, *args, **kwargs):
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


class login_view(View):
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'artists/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        return render(request, 'artists/login.html', {'form': form})
