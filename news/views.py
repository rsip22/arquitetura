from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post


def home_page(req):
    items = Post.objects.all().filter(
                published_date__lte=timezone.now()).order_by('published_date')
    return render(req, 'home.html', {'items': items})


def post_detail(req, pk):
    item = get_object_or_404(Post, pk=pk)
    return render(req, 'post_detail.html', {'item': item})
