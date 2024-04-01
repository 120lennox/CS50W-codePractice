from django.urls import path
from .views import HomepageView

urlpatterns = [
    path("<str:name>", HomepageView.as_view(), name='index'),
]
