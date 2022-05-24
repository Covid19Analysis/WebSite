from django.urls import path
from . import views

app_name = "twitterdata"

urlpatterns = [
    path("", views.index, name="index"),  
]