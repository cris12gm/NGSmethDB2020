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
from .models import getAllChroms, getAllSamples
from utilities.manageID import generate_uniq_id

class browser(TemplateView):
    template = 'browser/browser.html'
    
    def get(self,request):
        chroms = getAllChroms("hg38")
        samples = getAllSamples("hg38")

        uniqueID = generate_uniq_id()

        return render(request, self.template, {
            'chroms':chroms,
            'samples':samples,
            'uniqueID':uniqueID
        })
    def post(self,request):
        return render(request, self.template, {
        })