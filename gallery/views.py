from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Post
from .utils import get_client_ip
def gallery(request):
    return render(request, "gallery.html")


def index(request):
    context = {
        "title": "Galeri",
        "posts": Post.objects.all(),
        "client_ip": get_client_ip(request),
    }
    return render(request, "gallery.html", context)
