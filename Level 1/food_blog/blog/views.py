from django.shortcuts import render
from django.urls import URLPattern
from django.http import HttpResponse

# Create your views here.

posts_dict = {

    "1": {
        "title": "I love copper!",
        "image": "Copper",
        "content": "Ever since I was a kid I was amazed by the metalic smell and the fine, almost silky texture that the copper coils at the local construction site. I'm now 48 years old, 230lbs and putting copper grains in my food daily!",
        "author": "CopperChomper736",
        "publish_date": "01. 01. 1999.",
    },
    "2": {
        "title": "Spicy!",
        "image": "Uranium",
        "content": "It all started when I enrolled in my local university as a chem major. I always had a strange niche for radioactivity, but when I looked at the uranium capsule we had in one of our laboratories, I just couldn't help myself. I had to know what it tasted like. There was no other option. After some meticulous planning I was able to give myself a small opportunity to snatch the thing, and snatch it I did! As soon as it grazed my tounge it felt like 2000 volts of electricity shooting through my veins. It's finally happening. As I was indulging in a taste no words could ever explain, I could see bits of my tongue dripping down onto the carpet. I'm now writing from a hospital bed in the ICU, but it was damn worth it!",
        "author": "Uranimbicile3",
        "publish_date": "05. 12. 2049."
    }

}

def home(request):
    print("called", posts_dict)
    return render(request, "blog/home.html", {"posts": posts_dict})

def about(request):
    return render(request, "blog/about.html")

def posts(request, post_id):
    return render(request, "blog/posts.html", {"post": posts_dict[str(post_id)]})

def contact(request):
    return render(request, "blog/contact.html")