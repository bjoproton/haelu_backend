# General imports
from rest_framework import serializers
from django.contrib.auth import get_user_model

# Haelu


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'uuid', 'first_name', 'last_name']
