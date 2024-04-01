from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime as dt

# Create your views here.
class ViewLogic(TemplateView):
    template_name = 'logic\condition.html'
    
    def get(self, request):
        now = dt.now()
        birthday = now.month == 2 and now.day == 25
        remaining_days = 25 - now.day
        
        context = {
            'birthday' : birthday,
            'remaining_days' : remaining_days
        }
        
        return render(request, self.template_name, context)