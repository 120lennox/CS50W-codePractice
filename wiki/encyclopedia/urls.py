from django.urls import path
from .views import ListTitles, EntryDetailView, EntryForm, RandomPageView, SearchView, EntryUpdateView 


urlpatterns = [
    path("", ListTitles.as_view(), name="index"),
    path("wiki/<int:pk>/", EntryDetailView.as_view(), name="wiki"),
    path('add', EntryForm.as_view(), name='entry_form'), 
    path('random', RandomPageView.as_view(), name='random_entry'),
    path('search', SearchView.as_view(), name='search'), 
    path("<int:pk>/edit", EntryUpdateView.as_view(), name='edit')
]
