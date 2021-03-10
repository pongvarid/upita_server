from rest_framework.serializers import ModelSerializer

from ita.api.serializers import AgencySerializer
from report.models import ReportAll, ReportDetail, ReportRawIIT, ReportRawEIT


class ReportAllSerializer(ModelSerializer):

    class Meta:
        model = ReportAll
        fields = '__all__'

class ReportAllSerializerAll(ModelSerializer):
    agency = AgencySerializer()
    class Meta:
        model = ReportAll
        fields = '__all__'

class ReportDetailSerializer(ModelSerializer):
     
    class Meta:
        model = ReportDetail
        fields = '__all__'

class ReportDetailSerializerAll(ModelSerializer):
    agency = AgencySerializer()
    class Meta:
        model = ReportDetail
        fields = '__all__'

class ReportRawIITSerializer(ModelSerializer):

    class Meta:
        model = ReportRawIIT
        fields = '__all__'


class ReportRawEITSerializer(ModelSerializer):

    class Meta:
        model = ReportRawEIT
        fields = '__all__'
