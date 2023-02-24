from datapipelines.pipeline import DataPipeline
from markers.models import Marker, MarkerResult

import pytest


@pytest.mark.django_db
class TestDataPipeline:
    def test_no_markers(self, patient_user):
        dp = DataPipeline(data_required=['age', ], patient=patient_user)
        dp.load_all_data_items()
        assert dp.data == {'age': None}

    def test_marker_no_results(self, patient_user, markers):
        dp = DataPipeline(data_required=['age', 'urine infection', 'systolic bp', 'mental state concern'], patient=patient_user)
        dp.load_all_data_items()
        assert dp.data == {
            'age': None,
            'urine infection': None,
            'systolic bp': None,
            'mental state concern': None,
        }

    @pytest.mark.parametrize('in_values,out_values', [({'age': '73', 'urine infection': 'False', 'systolic bp': 22, 'mental state concern': 'True'},
                                                       {'age': 73, 'urine infection': False, 'systolic bp': 22, 'mental state concern': True}),
                                                      ({'age': '73', 'urine infection': 'False', 'systolic bp': 22},
                                                       {'age': 73, 'urine infection': False, 'systolic bp': 22, 'mental state concern': None}),
                                                      ])
    def test_marker_some_results(self, patient_user, markers, in_values, out_values):
        for k, v in in_values.items():
            m = Marker.objects.get(name=k)
            MarkerResult(marker=m, result=v, patient=patient_user).save()

        dp = DataPipeline(data_required=['age', 'urine infection', 'systolic bp', 'mental state concern'], patient=patient_user)
        dp.load_all_data_items()
        assert dp.data == out_values
