from django import forms
from .models import Application, Note
# Interview


# class InterviewForm(forms.ModelForm):
#     class Meta:
#         model = Interview
#         fields = ('date', 'interview')

class NoteForm(forms.ModelForm):
    class Meta: 
        model = Note
        fields = ('name', 'body')
        

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }

