from django.contrib import admin
from .models import Post

# Allow our blog post to be accessible from the admin area

admin.site.register(Post)
