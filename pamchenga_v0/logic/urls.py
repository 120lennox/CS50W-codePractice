from django.urls import path
from .views import ViewLogic

urlpatterns = [
    path("", ViewLogic.as_view(), name='condition')
]
