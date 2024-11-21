from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    # it's a string value which contains letters, hyphens, numbers or underscores.
    slug = models.SlugField(max_length = 200, unique = True)
    # one to many relationship , User can write more than one posts and models.CASCADE means that 
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "blog_posts")
    content = models.TextField()
    # default created time is the time of the entry post
    created_on = models.DateTimeField(auto_now_add=True)
    # It has 2 values either 0 for draft or 1 for published
    status = models.IntegerField(choices=STATUS, default=0)
