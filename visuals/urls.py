from django.urls import path
from .views import data_view
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='chart.html'), name='charts'),
]