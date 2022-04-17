from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Post
# Create your views here.


def index(request):
    context = {
        "title": "Blog",
        "posts": Post.objects.all()
    }
    return render(request, "blog.html", context)
