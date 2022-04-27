from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Post

def gallery(request):
    return render(request, "gallery.html")


def index(request):
    context = {
        "title": "Galeri",
        "posts": Post.objects.all()
    }
    return render(request, "gallery.html", context)
