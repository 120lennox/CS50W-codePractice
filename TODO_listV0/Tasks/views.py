from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import TaskForms
from .models import Tasks


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'tasks/index.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = Tasks.objects.all()
        
        return context

class AddTask(CreateView):
    template_name = 'tasks/add.html'
    model = Tasks
    form_class = TaskForms
    success_url = reverse_lazy('tasks:index')