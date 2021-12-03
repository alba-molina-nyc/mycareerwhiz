from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
# allows to list a queryset and then bring them back to website, queryset brings back one record, createview allows you to create
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Application, Note
#  Interview
from django.contrib.auth.models import User
from .forms import NoteForm
# InterviewForm


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

class UpdateApplicationView(UpdateView): 
    model = Application
    fields = '__all__'
    template_name = 'update_application.html'
    

class AddNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'add_note.html'
    success_url = reverse_lazy('home')
#adding kwargs and primary key
    def form_valid(self, form):
        form.instance.application_id = self.kwargs['pk']
        return super().form_valid(form)


