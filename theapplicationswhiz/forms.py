from django import forms
from .models import Application, Note, Interviewing


class InterviewingForm(forms.ModelForm):
    class Meta:
        model = Interviewing
        fields = ('date', 'interview')

class NoteForm(forms.ModelForm):
    class Meta: 
        model = Note
        fields = ('name', 'body')
        

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }

