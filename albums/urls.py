from django.urls import path
from . import views

urlpatterns =[
    path('create/',views.create_view.as_view(),name='create'),
]
