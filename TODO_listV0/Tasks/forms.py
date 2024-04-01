from .models import Tasks
from django import forms 

class TaskForms(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['enter_tasks']