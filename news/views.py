from django.shortcuts import render

from .models import Post


def home_page(req):
    items = Post.objects.all()
    return render(req, 'home.html', {'items': items})
