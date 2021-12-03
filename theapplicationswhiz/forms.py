from django import forms
from .models import Application, Note
# Interview


class NoteForm(forms.ModelForm):
    class Meta: 
        model = Note
        fields = ('name', 'body')
        

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }

