from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Home',
        'content': "Главная страница магазина Home",
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_auth': False
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')
