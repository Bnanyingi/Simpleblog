from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView 

urlpatterns = [
      path('',HomeView.as_view(), name="home"),
      path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
      path('addpost/', AddPostView.as_view(), name='addpost'),
      
]