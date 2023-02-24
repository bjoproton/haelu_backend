from rest_framework import serializers
from markers.models import Marker, MarkerResult


class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = ['id', 'name', 'value_type', ]


class MarkerResultSerializer(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()
    
    class Meta:
        model = MarkerResult
        fields = ['id', 'patient', 'marker', 'result', 'datetime', ]        
        read_only_fields = ('id', 'datetime')

    def get_datetime(self, obj):
        return obj.datetime.strftime("%d %b %Y %H:%M")
