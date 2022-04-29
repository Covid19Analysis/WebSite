from django.shortcuts import render
from .utils import get_client_ip
# Create your views here.




def index(request):
    context = {
        "title": "Twitter",
       
        "client_ip": get_client_ip(request),
    }
    return render(request, "twitterdata.html", context)