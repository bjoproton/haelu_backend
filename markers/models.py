# General imports
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Haelu imports
from haelu.enums import VALUE_TYPE_CHOICES, VALUE_TYPE_BOOLEAN


class Marker(models.Model):
    """ Model to hold marker data.

        Note use of "marker" rather than "symptom" as symptom
        implies link to disease, but this will be established
        elsewere.

        Here marker is e.g.
        name = blood pressure (systolic)
    """
    name = models.CharField(max_length=64, null=False,
                            blank=False, default='', unique=True)
    value_type = models.PositiveSmallIntegerField(null=False, blank=False,
                                                  choices=VALUE_TYPE_CHOICES,
                                                  default=VALUE_TYPE_BOOLEAN)
    unit = models.CharField(max_length=12, null=False,
                            blank=True, default='')

    class Meta:
        verbose_name = 'Marker'
        verbose_name_plural = 'Markers'

    def __str__(self):
        return f'{self.name}'


class MarkerResult(models.Model):
    """ Model to hold result values for a marker.
    """
    patient = models.ForeignKey(get_user_model(), null=False, blank=False,
                                on_delete=models.CASCADE)
    marker = models.ForeignKey('Marker', null=False, blank=False,
                               on_delete=models.CASCADE)
    result = models.CharField(max_length=64, null=False,
                              blank=False, default='')
    datetime = models.DateTimeField(blank=False, null=False, default=timezone.now)

    class Meta:
        verbose_name = 'Marker Result'
        verbose_name_plural = 'Marker Results'

    def __str__(self):
        return f'{self.patient.uuid} - {self.marker} - {self.result} - {self.datetime}'
