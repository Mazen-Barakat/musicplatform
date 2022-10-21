from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='artist'),
    path('create/', views.create_view, name='create'),
]
