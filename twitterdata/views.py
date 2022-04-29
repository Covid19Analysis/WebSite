from django.shortcuts import render
from .utils import get_client_ip
# Create your views here.

import pandas as pd
import numpy as np
import json
import csv
from datetime import datetime
#

import plotly.express as px
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

def index(request):
    df=pd.read_csv( "analiz_edilmis_gun.csv")
    x=df['Gün']
    y=df["Toplam Tweet"]  
    plot_div = plot([Scatter(x=x, y=y,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "index.html", context={'plot_div': plot_div})




#def index(request):
  #  context = {
  #      "title": "Twitter Verileri",
       
  #      "client_ip": get_client_ip(request),
  #  }
  #  return render(request, "twitterdata.html", context)