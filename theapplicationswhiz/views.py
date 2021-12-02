from django.shortcuts import render
#allows to list a queryset and then bring them back to website, queryset brings back one record
from django.views.generic import ListView, DetailView
from .models import Application

# Create your views here



# this is an example of a class view 
class HomeView(ListView):
    model = Application
    template_name = 'home.html'

class ApplicationsView(ListView):
    model = Application
    template_name = 'applications.html'

class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'application_detail.html'