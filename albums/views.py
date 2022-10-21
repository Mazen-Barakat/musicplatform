from django.shortcuts import render
from . import forms

# Create your views here.
def create_view(request):
    if request.method == 'POST':
        form = forms.CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CreateAlbumForm()
    return render(request,'albums/create.html' , {'form': form})
