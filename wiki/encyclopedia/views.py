from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView,View, UpdateView
from django.views.generic.detail import DetailView
from .models import Entries
from .forms import EntryForms
import markdown
from haystack.query import SearchQuerySet
from django.urls import reverse_lazy
import random
import re
from django.db.models import Q
from django.utils.html import strip_tags

from . import util

class ListTitles(ListView):
    template_name = 'encyclopedia/index.html'
    context_object_name = 'entries'
    
    def get_queryset(self):
         markdown_titles = util.list_entries()
         saved_titles = Entries.objects.values_list('title', flat=True)
         
         all_titles = list(set(markdown_titles + list(saved_titles)))
         
         return all_titles
         
class EntryDetailView(DetailView):
    model = Entries
    template_name = 'encyclopedia/entries.html'
    context_object_name = 'entry'
    
    def get_object(self, querySet=None):
        """"
        this function gets an entry from the user and compares if it matches with objects created on content(data from get_entry). Entries instance is created for persistent passing of data
        """
        #title = self.kwargs.get('title')
        pk = self.kwargs.get('pk')
        content = util.get_entry(pk)
        md = markdown.Markdown(extensions=['fenced_code'])
        #fixing 'NoneType' object has no attribute 'strip' error
        if content is not None:
            title_md = md.convert(pk)
            content_md = md.convert(content)
            return Entries(title=title_md, content=content_md)
        
        #check if entry is saved in database
        database_entry = Entries.objects.filter(pk=pk).first()
        sanitized_title = strip_tags(database_entry.title)
        if sanitized_title is not None:
            return sanitized_title 
        
        raise Http404('Entry not found')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entries'] = util.list_entries()
        return context

class EntryForm(CreateView):
    template_name = 'encyclopedia/add_form.html'
    form_class = EntryForms
    model = Entries
    success_url = reverse_lazy('index')
    
    def is_valid(self, form):
        title = form.cleaned_data('title')

        if Entries.objects.filter(title=title).exists():
            form.add_error('title', 'title already exists')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
class EntryUpdateView(UpdateView):
    model = Entries
    template_name = 'encyclopedia/update_entry.html'
    fields = '__all__'  
    success_url = reverse_lazy('index')  

class RandomPageView(EntryDetailView):
    template_name = 'encyclopedia/random_page.html'
    
    def get(self, request, *args, **kwargs):
        random_entry = random.choice(Entries.objects.all())
        self.object = random_entry
        context = self.get_context_data(object=random_entry)
        return render(request, self.template_name, context)

class SearchView(View):
    template_name = 'encyclopedia/search_results.html'

    def get(self, request):
        query = request.GET.get("q")
        results = self.get_queryset(query)
        return render(request, self.template_name, {
            "results":results,
            "query": query
        })
    
    def get_queryset(self, query):
        if query:
            results = Entries.objects.filter(
                Q(title__icontains=query)
            )
        else:
            results = Entries.objects.none()
        
        return results