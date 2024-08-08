from django.shortcuts import render
from .models import Data

# Create your views here.
def data_view(request):
    data = Data.objects.all()
    return render(request, 'base.html', {'data': data})