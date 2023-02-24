# General
from django.urls import path

# Haelu
from decisions.views import DecisionTreeViewSet, DecisionTreeRunViewSet

urlpatterns = [
    path('decisiontrees', DecisionTreeViewSet.as_view({'get': 'list'})),
    path('decisiontrees/run', DecisionTreeViewSet.as_view({'post': 'run'})),
    path('decisiontrees/runs', DecisionTreeRunViewSet.as_view({'get': 'list'})),
]
