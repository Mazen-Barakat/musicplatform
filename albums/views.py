from django.shortcuts import render
from . import forms
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name='dispatch')
class create_view(View):
    form_class = forms.CreateAlbumForm

    def get(self, request , *args , **kwargs):
        form = self.form_class()
        return render(request, 'albums/create.html' , {'form': form})
    
    def post(self, request , *args , **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'albums/create.html' , {'form': form})
