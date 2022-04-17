from django.urls import path

from .views import index

app_name = "blog"


urlpatterns = [
    path("", index, name="index"),
    # path("export_csv", export_csv, name="export-csv"),
    # path("export_pdf", export_pdf, name="export-pdf"),
    # path("blog", blog, name="blog"),
]
