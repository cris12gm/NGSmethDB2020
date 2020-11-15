import plotly.graph_objs as go
from plotly.offline import plot
import pandas as pd
import plotly.express as px
from sqlalchemy import inspect

from django.conf import settings

def plotRegion(meth):
    
    div_obj = ""
    valuesPlot = {}
    valuesPlot["methRatio"] = []
    valuesPlot["CpG ID"] = []

    for element in meth:
        idElement = element["chrom"]+"_"+element["start"]
        valueMeth = element["methRatio"]
        valuesPlot["methRatio"].append(valueMeth)
        valuesPlot["CpG ID"].append(idElement)
      
    df = pd.DataFrame(data=valuesPlot)

    fig = px.strip(df, 'CpG ID', 'methRatio', stripmode="overlay")

    # fig.update_layout(height=500,legend_orientation="h",xaxis_tickfont_size=14)
    # fig.update_xaxes(title_text='')
    # fig.update_yaxes(title_text='<b>Meth Ratio</b>',range=[-0.1, 1.1])
    div_obj = plot(fig, show_link=False, auto_open=False, output_type = 'div')

    return div_obj