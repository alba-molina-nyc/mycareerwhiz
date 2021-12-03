from django import forms
from .models import Application, Note, Category
# Interview

#hardcodes the choices but not good bc cant make changes easily 
# category_choices = [('Not Hired','Not Hired'), ('Hired', 'Hired'), ('Rejected Offer', 'Rejected Offer'), ('Accepted Offer', 'Accepted Offer'), ('Negotiation Stage', 'Negotiation Stage'), ('Received Offer', 'Received Offer'), ('Scheduled Final Interview','Scheduled Final Interview'), ('Scheduled Technical Interview', 'Scheduled Technical Interview'), ('Scheduled Team Interview', 'Scheduled Team Interview'), ('Scheduled Interview with Hiring Manager', 'Scheduled Interview with Hiring Manager'), ('Send Thank You Email', 'Send Thank You Email'), ('Scheduled Interview with Recruiter', 'Scheduled Interview with Recruiter'), ('Submitted Application', 'Submitted Application'), ('Working on Application', 'Working on Application')]

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices: 
    choice_list.append(item)


class ApplicationForm(forms.ModelForm):
    class Meta: 
        model = Application
        fields = ( 'user', 'title', 'company_name', 'salary', 'job_post', 'category', 'location', 'company_size', 'company_website', 'remote', 'category' )

    widgets = {
        'user': forms.Select(attrs={'class': 'form-control'}),
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'company_name': forms.TextInput(attrs={'class': 'form-control'}),
        'salary': forms.NumberInput(attrs={'class': 'form-control'}),
        'job_post': forms.TextInput(attrs={'class': 'form-control'}),
        'location': forms.TextInput(attrs={'class': 'form-control'}),
        'company_size': forms.TextInput(attrs={'class': 'form-control'}),
        'company_website': forms.URLInput(attrs={'class': 'form-control'}),
        'remote': forms.TextInput(attrs={'class': 'form-control'}),
        'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
    }

class NoteForm(forms.ModelForm):
    class Meta: 
        model = Note
        fields = ('name', 'body')
        

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }

