from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def Index(request):
    posts = Post.objects.all()
    return render(request, "post/index.html", {"posts": posts})

def Detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post/post_details.html", {"post": post})
