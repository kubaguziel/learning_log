from django.shortcuts import render

# Create your views here.

def index(request):
    """Strona główna aplikacjji Learning Log"""
    return render(request, 'learning_logs/index.html')
