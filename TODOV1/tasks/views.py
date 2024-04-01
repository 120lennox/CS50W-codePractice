from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from .models import Tasks
from .forms import TaskForms

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'tasks/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Tasks.objects.all()
        
        return context
    
class AddtaskView(CreateView):
    template_name = 'tasks/add.html'
    model = Tasks
    form_class = TaskForms
    success_url = reverse_lazy('tasks:home')