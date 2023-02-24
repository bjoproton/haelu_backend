# General
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_authtoken.auth import AuthTokenAuthentication
from django.contrib.auth import get_user_model

# Haelu
from decisions.serializers import DecisionTreeSerializer, DecisionTreeRunSerializer
from decisions.models import DecisionTree, Condition, DecisionTreeRuns
from datapipelines.pipeline import DataPipeline
from decisions.decisiontreebuilder import DecisionTree as DTB


class DecisionTreeViewSet(viewsets.ModelViewSet):
    queryset = DecisionTree.objects.all()
    serializer_class = DecisionTreeSerializer
    authentication_classes = (AuthTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def run(self, request, *args, **kwargs):
        patient_id = request.data.get('patient')
        decision_tree_id = request.data.get('decision_tree')

        patient = get_user_model().objects.get(id=patient_id)
        decision_tree = DecisionTree.objects.get(id=decision_tree_id)

        data_points = [c.value_name for c in Condition.objects.all()]
        dp = DataPipeline(data_points, patient)
        dp.load_all_data_items()

        # Run it
        try:
            t = DTB(decision_tree)
            r = t.evaluate(dp.data)
        except BaseException:
            r = None
        if not r:
            r = "An error occurred with the data"

        DecisionTreeRuns(patient=patient, decision_tree=decision_tree, result=r).save()

        # Add alert
        return Response(r, status=status.HTTP_200_OK)


class DecisionTreeRunViewSet(viewsets.ModelViewSet):
    queryset = DecisionTreeRuns.objects.all().order_by('-datetime')
    serializer_class = DecisionTreeRunSerializer
    authentication_classes = (AuthTokenAuthentication, )
    permission_classes = (IsAuthenticated, )
