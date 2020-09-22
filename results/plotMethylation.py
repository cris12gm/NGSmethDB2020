import plotly.graph_objs as go
from plotly.offline import plot
import pandas as pd
import plotly.express as px
from sqlalchemy import inspect

from django.conf import settings

def plotRegion(meth,sample):
    
    div_obj = ""

    for element in meth:
        print (element)
    # for key in associated:
    #     cpgs[int(key)]=True

    # # #Get meth

    # valuesPlot = {}
    # valuesPlot["methRatio"] = []
    # valuesPlot["CpG ID"] = []
    # valuesPlot["Sample"] = []
    # valuesPlot["Associated"] = []

    # numCpGs = 0
    # for i in range(start,end):
    #     idElement = chrom+"_"+str(i)
    #     methylationCpG = getMethylation.getMethCpG(idElement)
    #     if methylationCpG:
    #         numCpGs = numCpGs + 1
    #         inst = inspect(methylationCpG)
    #         attr_names = [c_attr.key for c_attr in inst.mapper.column_attrs]
    #         for att in attr_names:
    #             valueMeth = getattr(methylationCpG,att)
                
    #             if valueMeth and not "_" in str(valueMeth):
    #                 valuesPlot["methRatio"].append(valueMeth)
    #                 valuesPlot["CpG ID"].append(idElement)
    #                 valuesPlot["Sample"].append(att)  
    #                 try:
    #                     cpgs[i]
    #                     valuesPlot["Associated"].append("YES")
    #                 except:
    #                     valuesPlot["Associated"].append("NO")
    
    # df = pd.DataFrame(data=valuesPlot)

    # fig = px.strip(df, 'CpG ID', 'methRatio', 'Associated', hover_data=["Sample"],stripmode="overlay",width=250*numCpGs)

    # fig.update_layout(height=500,legend_orientation="h",xaxis_tickfont_size=14)
    # fig.update_xaxes(title_text='')
    # fig.update_yaxes(title_text='<b>Meth Ratio</b>',range=[-0.1, 1.1])
    # div_obj = plot(fig, show_link=False, auto_open=False, output_type = 'div')

    return div_obj