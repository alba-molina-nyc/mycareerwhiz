from typing import List
from django.shortcuts import render
#allows to list a queryset and then bring them back to website, queryset brings back one record
from django.views.generic import ListView, DetailView
from theapplicationswhiz.models import Application

# Create your views here



# this is an example of a class view 
class HomeView(ListView):
    model = Application
    template_name = 'home.html'
