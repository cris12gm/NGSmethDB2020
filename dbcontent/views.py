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

from .models import getDBContent

class dbcontent(TemplateView):
    template = 'dbcontent.html'

    def get(self,request):

        content = getDBContent("databaseContent")

        return render(request, self.template, {'content' : content})
    def post(self,request):
        return render(request, self.template, {
        })