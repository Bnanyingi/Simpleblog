from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
#Define our Superuser and body of the page
class Post(models.Model):
     title = models.CharField(max_length=255)
     title_tag = models.CharField(max_length=255)
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     body = models.TextField()
     
     
     #allow admin to see the title of the blog post and the author
     
     def __str__(self):
         return self.title + ' | ' + str(self.author)
     
     #redirects the admin page to the post page
     def get_absolute_url(self):
         #return reverse('article', args=(str(self.id)) )
         return reverse('home')
