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
from results.saveMethFile import saveFileMeth

from utilities.manageID import checkID


# Create your views here.

class region(TemplateView):
    template = 'results/region.html'
    templateError = 'results/notFoundResults.html'
    
    def get(self,request):

        id_send = request.GET['id']
        idStatus = checkID(id_send)

        if idStatus:
            return render(request, self.template, { 
                'uniqueID' : id_send
            })
        else:

            return render(request, self.templateError, {} )

    
    def post(self,request):

        chrom = request.POST['chrom'].split("_")[0]
        chromStart = int(request.POST['chromStart'])
        chromEnd = int(request.POST['chromEnd'])
        samples = [request.POST['sample']]
        inputID = request.POST['input_id']
        
        meth = getRegionMeth("hg38",chrom,chromStart,chromEnd)

        meth2 = saveFileMeth(inputID,meth,samples)

        return render(request, self.template, { 'uniqueID':inputID
        })

# class region_get(TemplateView):
#     template = 'results/region.html'

#     def get(self,request):
#         return render(request, self.template, {
#         })
    
#     def post(self,request):
#         return render(request, self.template, {
#         })
    
    