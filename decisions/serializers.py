# General imports
from rest_framework import serializers

# Haelu
from decisions.models import DecisionTree, DecisionTreeRuns


class DecisionTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisionTree
        fields = ['id', 'name']


class DecisionTreeRunSerializer(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()
    
    class Meta:
        model = DecisionTreeRuns
        fields = ['id', 'patient', 'decision_tree', 'result', 'datetime']
        read_only_fields = ('datetime', )

    def get_datetime(self, obj):
        return obj.datetime.strftime("%d %b %Y %H:%M")
