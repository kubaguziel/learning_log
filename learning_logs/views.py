from django.shortcuts import render

from .models import Topic
# Create your views here.

def index(request):
    """Strona główna aplikacji Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Wyświetlenie listy wszystkich tematów"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html',context)