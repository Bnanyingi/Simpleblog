from django.db import models
from django.contrib.auth.models import User
#Define our Superuser and body of the page
class Post(models.Model):
     title = models.CharField(max_length=255)
     title_tag = models.CharField(max_length=255, default="BestFriendsForever")
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     body = models.TextField()
     
     #allow admin to see the title of the blog post and the author
     
     def __str__(self):
         return self.title + ' | ' + str(self.author)
     
