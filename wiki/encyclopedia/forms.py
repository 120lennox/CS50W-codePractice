from django import forms 
from .models import Entries

class EntryForms(forms.ModelForm):
    class Meta:
        model = Entries
        fields = ['title', 'content']