from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

#define our views 
#def home(request):
#return render(request, 'home.html', {})

#List all content on the homepage in ListView
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

#List all content on the article details page in DetailView
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article.html'   
    
class AddPostView(CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
        
    #fields = '__all__'
    
    
