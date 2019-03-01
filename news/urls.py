from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
