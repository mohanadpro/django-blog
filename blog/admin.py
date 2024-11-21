from django.contrib import admin
from .models import Post

# Register your models here.
# This allows me to create, edit, delete post from admin page
admin.site.register(Post)