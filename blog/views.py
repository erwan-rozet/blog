from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(requests):
#     return render(requests, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name  = 'home.html'
    # ordering = ['-id'] # inverser l'ordre des publications en attendant datetime
    ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm # cette ligne gère la mise ne forme du form, basculer sur fields pour retourner au basic form
    template_name  = 'add_post.html'
    # fields = '__all__'
    # fields = ['title, 'body'] ### Pour ajouter seulement certains fields

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm  # une autre class de Form
    template_name  = 'update_post.html'
    # fields = '__all__'
    # fields = ['title', 'title_tag', 'body'] 

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')