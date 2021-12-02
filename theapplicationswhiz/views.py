from django.shortcuts import render, redirect
# allows to list a queryset and then bring them back to website, queryset brings back one record, createview allows you to create
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Application
from django.contrib.auth.models import User

# Create your views here

# def home(request):
#     # send sample cat objects here
#     return render(request, 'home.html')

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

class AddApplicationView(CreateView):
    model = Application
    fields = '__all__'
    template_name = 'add_application.html'



