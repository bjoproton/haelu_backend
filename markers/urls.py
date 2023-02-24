# General
from django.urls import path

# Haelu
from markers.views import MarkerViewSet, MarkerResultViewSet

urlpatterns = [
    path('markers', MarkerViewSet.as_view({'get': 'list'})),
    path('markers/<int:pk>', MarkerViewSet.as_view({'get': 'retrieve'})),
    path('results/<uuid:patient_uuid>', MarkerResultViewSet.as_view({'get': 'list'})),
    path('results', MarkerResultViewSet.as_view({'get': 'list', 'post': 'create'})),
]
