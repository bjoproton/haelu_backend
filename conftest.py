import pytest
from rest_framework.test import APIClient
from account.models import User
from markers.models import Marker

@pytest.fixture
def request_client():
    return APIClient()


@pytest.fixture
def patient_user():
    try:
        user = User.objects.get(username='patient_user')
    except User.DoesNotExist:
        user = User(username='patient_user')
        user.save()
    return user


@pytest.fixture
def markers():
    Marker(name='age', value_type=Marker.VALUE_TYPE_INTEGER, unit='years').save()
    Marker(name='urine infection', value_type=Marker.VALUE_TYPE_BOOLEAN, unit='').save()
    Marker(name='systolic bp', value_type=Marker.VALUE_TYPE_INTEGER, unit='mmHg').save()
    Marker(name='mental state concern', value_type=Marker.VALUE_TYPE_BOOLEAN, unit='').save()
    return Marker.objects.all()
