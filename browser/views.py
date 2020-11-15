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

from datetime import datetime
import csv
from sqlalchemy import inspect
from .models import getContent, getAllChroms, getAllSamples
from utilities.manageID import generate_uniq_id

def processContent(content):
    assemblies = {}

    for sample in content:
        assembly = sample['assembly']
        try:
            samples = assemblies[assembly]
        except:
            samples = []
        samples.append(sample)
        assemblies[assembly] = samples

    content = {}
    for assembly in assemblies:
        samples = assemblies[assembly]
        samplesProcess = {}
        for sample in samples:
            sampleT = sample["sample"]
            try:
                allS = samplesProcess[sampleT]
            except:
                allS = []
            allS.append(sample)
            samplesProcess[sampleT] = allS
        content[assembly] = samplesProcess        
    return content

class browser(TemplateView):
    template = 'browser/browser.html'
    
    def get(self,request):
        content = getContent("databaseContent")
        contentEdit = processContent(content)

        chroms = getAllChroms("hg38")
        samples = getAllSamples("hg38")
        # tissue = getAllTissues()

        uniqueID = generate_uniq_id()

        return render(request, self.template, {
            'content':contentEdit,
            'chroms':chroms,
            'samples':samples,
            'uniqueID':uniqueID
        })
    def post(self,request):
        return render(request, self.template, {
        })