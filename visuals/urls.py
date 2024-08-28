from django.urls import path
from .views import DataFormView, home, Analytics, GraphPageView, StaticGraphView


urlpatterns = [
    path('', home.as_view(), name='charts'),
    path('data/', DataFormView.as_view(), name='data'),
    path('analytics/', Analytics.as_view(), name='analytics'),
    path('graph-view', GraphPageView.as_view(), name='graph_page'),
    path('static-graph/', StaticGraphView.as_view(), name='static_graph'),
]