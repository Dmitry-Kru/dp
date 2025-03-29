from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import News
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')


def news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news_item = form.save(commit=False)
            news_item.user = request.user
            news_item.save()
            return redirect('news')
    else:
        form = NewsForm()

    return render(request, 'news.html', {
        'form': form,
        'news_list': News.objects.all(),
        'request': request  # Важно передать request в контекст
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form,
        'request': request
    })