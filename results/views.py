import itertools
from django.conf import settings
import datetime
import os
from enum import Enum
from functools import reduce
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import FormView, DetailView, TemplateView
from django.http import JsonResponse
from django.urls import reverse_lazy

from .models import getRegionMeth
from results.plotMethylation import plotRegion
# Create your views here.

class region(TemplateView):
    template = 'results/region.html'
    
    def get(self,request):

        return redirect(settings.SUB_SITE+"/browser")

    def post(self,request):

        chrom = request.POST['chrom'].split("_")[0]
        chromStart = int(request.POST['chromStart'])
        chromEnd = int(request.POST['chromEnd'])
        sample = request.POST['sample']
        
        meth = getRegionMeth("hg38",chrom,chromStart,chromEnd)

        plot = plotRegion(meth,sample)

        return render(request, self.template, {
        })