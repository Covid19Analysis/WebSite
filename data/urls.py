from django.urls import path

from .views import chart_select_view, export_csv, export_pdf

app_name = "data"


urlpatterns = [
    path("", chart_select_view, name="main-data"),
    path("export_csv", export_csv, name="export-csv"),
    path("export_pdf", export_pdf, name="export-pdf"),
    
]
