from django.shortcuts import render

# self added
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404
# Create your views here.

class MyPostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    **Template:**
    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    context = { "post":post }
    return render(
        request,
        "blog/post_detail.html",
        {"context": context},
    )