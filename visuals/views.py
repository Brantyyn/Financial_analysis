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

    def form_valid(self, form):
        # This method is called when valid form data has been posted.
        # Here you need to save the form data to the database.
        form.save()  # Ensure your DataForm is a ModelForm or has a save method
        return super().form_valid(form)


    
class home(TemplateView):
    template_name = 'chart.html'



class Analytics(TemplateView):
    template_name = 'analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Data.objects.all()  # Retrieve all data objects from the database
        context['data'] = data  # Pass the data to the template
        return context
    




    
