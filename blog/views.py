from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def home(requests):
#     return render(requests, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name  = 'home.html'
