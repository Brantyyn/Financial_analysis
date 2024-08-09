from django.urls import path
from .views import DataFormView, home


urlpatterns = [
    path('', home.as_view(), name='charts'),
    path('data/', DataFormView.as_view(), name='data'),
]