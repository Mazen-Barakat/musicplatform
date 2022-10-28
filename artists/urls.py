from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view.as_view()),
    path('create/', views.create_view.as_view()),
    path('login/', views.login_view.as_view()),
]
