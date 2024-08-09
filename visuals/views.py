# views.py
from django.shortcuts import render
from .models import Data
from .forms import DataForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import DataForm



class DataFormView(FormView):
    form_class = DataForm
    template_name = 'tables.html'
    success_url = reverse_lazy('charts')


    
class home(TemplateView):
    template_name = 'chart.html'



    
