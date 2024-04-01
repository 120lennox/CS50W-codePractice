from django.urls import path
from .views import *

app_name = "tasks"
urlpatterns = [
    path("add", AddtaskView.as_view(), name="add"),
    path("", HomePageView.as_view(), name="home")
]
