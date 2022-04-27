from django.shortcuts import render
from django.http.response import HttpResponse

def gallery(request):
    return HttpResponse("Galeri Sayfasi")
