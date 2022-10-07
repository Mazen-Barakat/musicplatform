import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def artist(request):
    return HttpResponse(f'<h1 style="color:red;">artist</h1>')
