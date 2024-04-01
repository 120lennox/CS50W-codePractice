from django import forms
from .models import Tasks

class TaskForms(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['Task_head', 'Task_body']