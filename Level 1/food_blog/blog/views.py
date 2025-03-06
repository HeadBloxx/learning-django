from django.shortcuts import render
from django.urls import URLPattern
from django.http import HttpResponse

# Create your views here.

posts_dict = {

    "1": {
        "title": "title1",
        "image": "Copper",
        "content": "content1",
        "author": "John Doe",
        "publish_date": "01.01.1999.",
    },
    "2": {
        "title": "title2",
        "image": "Uranium",
        "content": "content2",
        "author": "Jane Doe",
        "publish_date": "05.12.2049."
    }

}

def home(request):
    print("called", posts_dict)
    return render(request, "blog/home.html", {"posts": posts_dict})

def about(request):
    return render(request, "blog/about.html")

def posts(request, post_id):
    return render(request, "blog/posts.html", {"post": posts_dict[str(post_id)]})