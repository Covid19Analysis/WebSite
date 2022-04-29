from django.shortcuts import render
from .utils import get_client_ip
# Create your views here.

import pandas as pd
import numpy as np
import json
import csv
from datetime import datetime
#

from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
def index(request):
    df=pd.read_csv( "analiz_edilmis_gun.csv")
    fig = go.Figure([go.Scatter(x=df['gun'], y=df['nlikes'])])
    fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
    
    plt_div = plot(fig, output_type='div', include_plotlyjs=False)

    return render(request, "twitterdata.html", context={'plot_div': plot_div})



#def index(request):
  #  context = {
  #      "title": "Twitter Verileri",
       
  #      "client_ip": get_client_ip(request),
  #  }
  #  return render(request, "twitterdata.html", context)