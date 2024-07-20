from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm
# Create your views here.

def index(request):
    """Strona główna aplikacji Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Wyświetlenie listy wszystkich tematów"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    """Wyświetla pojedyńczy temat i wszystkie powiązane z nim wpisy"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html',context)

def new_topic(request):
    """Dodaj nowy temat."""
    if request.method != 'POST':
        #Nie przekazano żadnych danych, należy utworzyć nowy formularz
        form = TopicForm()
    else:
        #Przekazano dane za pomocą żadania POST, należy je przetworzyć
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    #Wyświetlenie pustego formularza
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html',context)

def new_entry(request, topic_id):
    """Dodaj nowy wpis"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nie przekazano zadnych danych
        form = EntryForm()
    else:
        #Przekazano dane za pomocą żądania POST, należy je przetworzyć
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    #wyświetlenie pustego formularza
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)