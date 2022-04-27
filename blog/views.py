from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Post
from .utils import get_client_ip
# Create your views here.


def index(request):
    context ={
        "title": "Blog",
        "client_ip": get_client_ip(request),
        "posts": Post.objects.all()
    }
    return render(request, "blog.html", context)
