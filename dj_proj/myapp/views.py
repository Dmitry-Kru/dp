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
            if not news_item.created_at:  # Если дата не указана
                news_item.created_at = timezone.now()
            news_item.save()
            return redirect('news')
    else:
        form = NewsForm()

    context = {
        'request': request,  # Передаем request в контекст
        'form': form,        # Используем существующую форму (не создаем новую)
        'news_list': News.objects.all().order_by('-created_at'),  # Добавил сортировку
    }
    return render(request, 'news.html', context)


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