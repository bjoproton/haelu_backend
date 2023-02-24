# General
from django.urls import path

# Haelu
from patients.views import PatientViewSet

urlpatterns = [
    path('patients', PatientViewSet.as_view({'get': 'list'})),
]
