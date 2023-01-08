from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# def home(requests):
#     return render(requests, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name  = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name  = 'add_post.html'
    # fields = '__all__'
    # field = ('title, 'body') ### Pour ajouter seulement certains fields