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

def processMeth(meth,sample):
    methP = []
    for element in meth:
        chrom = element['_id'].split("_")[0]
        start = element['_id'].split("_")[1]
        methRatio = element['methylation_CG'][sample]["methRatio"]
        pScore = element['methylation_CG'][sample]["pScore"]
        result = {"chrom":chrom,"start":start,"methRatio":methRatio,"pScore":pScore}
        methP.append(result)
    return methP

class region(TemplateView):
    template = 'results/region.html'
    templateError = 'results/notFoundResults.html'
    
    def get(self,request):

        id_send = request.GET['id']
        idStatus = checkID(id_send)

        # Check ID status
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
        query = chrom+":"+str(chromStart)+"-"+str(chromEnd)
        if request.POST['sample'] == "ALL":
            samples = "ALL"
        else:
            samples = [request.POST['sample']]
        inputID = request.POST['input_id']
        # method = request.POST['method']
        
        # Create jobDir

        rootID = settings.MEDIA_ROOT+"/"+inputID
        os.mkdir(rootID)

        #GetMeth

        meth = getRegionMeth("hg38",chrom,chromStart,chromEnd)
        methP = processMeth(meth,samples[0])
        linkFileMeth = saveFileMeth(inputID,meth,samples)
        linkFileMeth = ""

        return render(request, self.template, {
            'uniqueID':inputID,
            'linkFileMeth':linkFileMeth,
            'query':query,
            'samples':samples,
            'meth':methP
        })
