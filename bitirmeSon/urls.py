"""bitirmeSon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from atexit import register
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import data.views


urlpatterns = [
    path("", data.views.index, name="index"),
    path("admin/", admin.site.urls),
    path("login/", data.views.login, name="login"),
    path("register/", data.views.register, name="register"),
    path("about/", data.views.about, name="about"),
    path("countries/", data.views.country, name="country"),
    path("data/", include("data.urls", namespace='data'),name="data-index"),
    path("blog/", include("blog.urls", namespace='blog'),name="blog-index"),

    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
