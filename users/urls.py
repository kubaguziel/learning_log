"""Definiuje wzorce adresów dla aplikacji users"""
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    #dołączenie domyślnych adresów uwierzytelniania
    path('',include('django.contrib.auth.urls')),
]