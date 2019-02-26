from django.http import HttpResponse
from django.shortcuts import render


def home_page(req):
    return render(req, 'home.html')
