from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Tag


def home_page(req):
    """ Home page view with list of posts. """
    items = Post.objects.all().filter(
                published_date__lte=timezone.now()).order_by('published_date')
    return render(req, 'home.html', {'items': items})


def post_detail(req, pk):
    """ Page view to read one post. """
    item = get_object_or_404(Post, pk=pk)
    return render(req, 'post_detail.html', {'item': item})


def categories_list(req, pk):
    """ View to list posts belonging to a certain category. """
    category_posts = Post.objects.all().filter(
                        published_date__lte=timezone.now(),
                        tags=pk)
    category_name = get_object_or_404(Tag, pk=pk)
    return render(req,
                  'categories_list.html',
                  {'category_posts': category_posts,
                   'category_name': category_name})
