from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def index(request):
    now = datetime.now()
    data = {
        'ism': 'Bekzod',
        'vaqt': now
    }
    return render(request, 'post/index.html', context=data)


def about(request):
    data = {
        'nomi': 'DATA Learning Centre',
    }
    return render(request, "post/about.html", context=data)


def contact(request):
    return render(request, "post/contact.html")