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
import plotly.graph_objs as p
import plotly.express as px

   


def index(request):
    df=pd.read_csv( "analiz_edilmis.csv") #veriden yazı vs sil öyle ayıklık olar kyap
    x=df['date']
    y=df["nlikes"]  
    df1=pd.read_csv( "analiz_edilmis_gun.csv")
    a=df1['Gun']
    b=df1["Tweets_Skoru"]  
    plot_div = plot([p.Scatter(x=a, y=b,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    #bar_div=plot(px.line(df, x=x, y=df.columns, title='Günlere Göre Atılan Tweet Sayısı'),output_type='div')
    line_div=plot(px.line(df1,x=a, y=df1.columns, title='Günlere Göre Tweet İstatistiği'),output_type='div')  

      
    
    return render(request, "twitterdata.html", context={'plot_div': line_div})




#def index(request):
  #  context = {
  #      "title": "Twitter Verileri",
       
  #      "client_ip": get_client_ip(request),
  #  }
  #  return render(request, "twitterdata.html", context)