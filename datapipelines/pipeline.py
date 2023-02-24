# General imports

# Haelu imports
from haelu.enums import VALUE_TYPE_INTEGER, VALUE_TYPE_FLOAT, VALUE_TYPE_BOOLEAN
from markers.models import Marker, MarkerResult


class DataPipeline:
    """ Class responsible for preparing the data for consumption
        by the analysis elements.

        This is designed as a standalone app, as it needn't be
        part of a monolithic design and needn't be synchronous. 
        Can be run as part of a ETL pipeline for example.

        Various rules can be used here in the processesing and
        various techniques can be applied to massage the data
        into useful formats. 

        I have kept this delibirately simple for the purposes
        of this example, the class simply knows the data
        expected by the analysis tools and extracts it.
    """

    def __init__(self, data_required, patient):
        self.data_required = data_required
        self.patient = patient
        self.data = {}

    def load_all_data_items(self):
        for k in self.data_required:
            v = self._load_most_recent_data_item(k)
            self.data.update({k: v})
            
    def _load_most_recent_data_item(self, name):
        try:
            marker = Marker.objects.get(name=name)
        except Marker.DoesNotExist:
            marker = None

        if marker:
            res = MarkerResult.objects.filter(marker=marker, patient=self.patient).order_by('-datetime')
            
            if res:
                value = res.first().result
        
                if marker.value_type == VALUE_TYPE_INTEGER:
                    return int(value)
                elif marker.value_type == VALUE_TYPE_FLOAT:
                    return float(value)
                elif marker.value_type == VALUE_TYPE_BOOLEAN:
                    return value == 'True'

        return None
        
