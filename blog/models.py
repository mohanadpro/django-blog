from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    class Meta:
        # - is for descending ordering
        ordering = ["-created_on"]
    title = models.CharField(max_length = 200, unique = True)
    # it's a string value which contains letters, hyphens, numbers or underscores.
    slug = models.SlugField(max_length=200, unique=True)
    # one to many relationship , User can write more than one posts and models.CASCADE means that 
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "blog_posts")
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    # default created time is the time of the entry post
    created_on = models.DateTimeField(auto_now_add=True)
    #auto_now sets the value to the current date and time whenever the record is saved, not just when it is created. 
    updated_on = models.DateTimeField(auto_now=True)
    # It has 2 values either 0 for draft or 1 for published
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.title} {self.author}"

class Comment(models.Model):
    class Meta:
        ordering = ["created_on"]

    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.body} by {self.author}"