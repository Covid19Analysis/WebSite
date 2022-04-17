from django.http.response import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from xhtml2pdf import pisa
import pandas as pd
import numpy as np
import json
import csv
from datetime import datetime

from .utils import get_simple_plot, get_client_ip

# Create your views here.


def export_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        "attachment; filename=covIData-" + str(datetime.now()) + ".csv"
    )
    response["encoding"] = "utf-8"
    writer = csv.writer(response)
    writer.writerow(
        [
            "tarih",
            "bugunkuVaka",
            "bugunkuTest",
            "bugunkuVefat",
            "bugunkuIyilesen",
        ]
    )  # Türkçe karakter sorunu mevcut
    for item in df2.values:
        writer.writerow(
            [
                item[0],
                item[1],
                item[3],
                item[4],
                item[5],
            ]
        )
    # CSV indirme işlemleri
    return response


def export_pdf(request):
    template_path = "export_pdf.html"
    json_records = df2.reset_index().to_json(orient="records")
    data = []
    data = json.loads(json_records)

    toplam_veri = {  # df['MyColumn'].sum()
        "tVaka": df2["bugunkuVaka"].sum(),
        "tTest": df2["bugunkuTest"].sum(),
        "tVefat": df2["bugunkuVefat"].sum(),
        "tIyilesen": df2["bugunkuIyilesen"].sum(),
    }
    context = {
        "baslik": "Covid19 Veri Özeti",
        "data": data,
        "graph": graph,
        "sumOfdata": toplam_veri,
    }
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        "filename=covIDRapor-" + str(datetime.now()) + ".pdf"
    )  # attachment;
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Bazı sorunlar meydana geldi <pre>" + html + "</pre>")
    return response


def index(request):
    with open("userLog.log", "a") as file_object:
        file_object.write(
            "\nKullanıcı IP : "
            + get_client_ip(request)
            + "\tGiriş Saati : "
            + str(datetime.now())
        )
    context = {
        "title": "Ana Sayfa",
        "client_ip": get_client_ip(request),
    }
    return render(request, "main.html", context)


def login(request):
    context = {
        "title": "Login",

    }
    return render(request, "login.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        "title": "Register",
        "form": form
    }
    return render(request, "register.html", context)


def about(request):
    context = {
        "title": "About",
    }
    return render(request, "about.html", context)

def country(request):
    context = {
        "title": "Ülke Bazında Veriler",
        
    }
    return render(request, "countries.html", context)

def chart_select_view(request):
    global graph
    graph = None
    error_msg = None
    df = None
    global df2
    df2 = None
    covid19 = pd.read_csv(
        "data3.csv",
        parse_dates=True,
    )  # index_col="tarih"
    df = (
        covid19.copy()
        .rename({"tarih": "Tarih"}, axis=1)
        .drop(
            {
                "hastalardaZaturreOrani",
                "toplamTest",
                "toplamVaka",
                "toplamVefat",

                "toplamIyilesenHasta",
            },
            axis=1,
        )
    )
    df2 = df.copy()

    if df.shape[0] > 0:

        if request.method == "POST":
            chart_type = request.POST.get("grafik_turu")
            date_from = request.POST["date_from"]
            date_to = request.POST["date_to"]

            # df['Tarih'] = df['Tarih'].apply(lambda x: x.strftime("%d-%m-%Y"))
            df = df.astype({"Tarih": np.datetime64})
            df["Tarih"] = df["Tarih"].dt.strftime("%Y-%m-%d")
            # gunluk = df.loc[df["Tarih"].isin(["27-06-2021", "29-06-2021"])]
            df2 = df[(df["Tarih"] >= date_from) & (df["Tarih"] <= date_to)]
            if chart_type != "":
                if date_from != "" and date_to != "":
                    df2 = df[(df["Tarih"] >= date_from)
                             & (df["Tarih"] <= date_to)]
                    # print(datetime.datetime.strftime(date_from)
                    df2 = df2.astype({"Tarih": np.datetime64})
                    df2["Tarih"] = df2["Tarih"].dt.strftime("%d/%m/%Y")
                    # print(df2["Tarih"](0))
                    # print(datetime.strptime(date_from, '%m-%d-%Y').date())
                    title = date_from + " ile " + date_to + " arasındaki " + chart_type

                    # print(type(df2))
                    graph = get_simple_plot(
                        chart_type,
                        title,
                        x=df2["Tarih"],
                        y=df2["bugunkuVaka"],
                        data=df2,
                    )
                else:
                    error_msg = "trh"  # Tarih alanları boş
            else:
                error_msg = "grf"  # Grafik türü seçilmedi
    else:
        error_msg = "kyt"  # Kayıt yok
    # print(df2)
    json_records = df2.reset_index().to_json(orient="records")
    data = []
    data = json.loads(json_records)

    template_name = "data.html"
    toplam_veri = {  # df['MyColumn'].sum()
        "tVaka": df2["bugunkuVaka"].sum(),
        "tTest": df2["bugunkuTest"].sum(),
        "tVefat": df2["bugunkuVefat"].sum(),
        "tIyilesen": df2["bugunkuIyilesen"].sum(),
    }
    context = {
        "title": "Data Sayfası",
        "hata_msj": error_msg,
        "graph": graph,
        "data": data,
        "sumOfdata": toplam_veri,
    }
    return render(request, template_name=template_name, context=context)

    # print(
    #     gunluk.rename(
    #         {
    #             "bugunkuVaka": "Vaka",
    #             "bugunkuHasta": "Hasta",
    #             "bugunkuTest": "Test",
    #             "bugunkuVefat": "Vefat",
    #             "bugunkuIyilesen": "İyileşen",
    #         },
    #         axis=1,
    #     )
    # )
