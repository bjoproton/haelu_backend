# General
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_authtoken.auth import AuthTokenAuthentication
from django.contrib.auth import get_user_model

# Haelu
from patients.serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.filter(groups__name='Patient')
    serializer_class = PatientSerializer
    authentication_classes = (AuthTokenAuthentication, )
    permission_classes = (IsAuthenticated, )
