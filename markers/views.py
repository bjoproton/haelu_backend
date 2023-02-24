# General
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_authtoken.auth import AuthTokenAuthentication

# Haelu
from markers.models import Marker, MarkerResult
from markers.serializers import MarkerSerializer, MarkerResultSerializer


class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    authentication_classes = (AuthTokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class MarkerResultViewSet(viewsets.ModelViewSet):
    queryset = MarkerResult.objects.all()
    serializer_class = MarkerResultSerializer
    authentication_classes = (AuthTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if 'patient_uuid' in self.kwargs.keys():
            return self.queryset.filter(patient__uuid=self.kwargs['patient_uuid']).order_by('-datetime')
        else:
            return self.queryset.filter().order_by('-datetime')
