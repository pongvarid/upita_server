from rest_framework.viewsets import ModelViewSet
from report.serializers import ReportAllSerializer, ReportDetailSerializer, ReportRawIITSerializer, ReportRawEITSerializer
from report.models import ReportAll, ReportDetail, ReportRawIIT, ReportRawEIT


class ReportAllViewSet(ModelViewSet):
    queryset = ReportAll.objects.order_by('pk')
    serializer_class = ReportAllSerializer


class ReportDetailViewSet(ModelViewSet):
    queryset = ReportDetail.objects.order_by('pk')
    serializer_class = ReportDetailSerializer


class ReportRawIITViewSet(ModelViewSet):
    queryset = ReportRawIIT.objects.order_by('pk')
    serializer_class = ReportRawIITSerializer


class ReportRawEITViewSet(ModelViewSet):
    queryset = ReportRawEIT.objects.order_by('pk')
    serializer_class = ReportRawEITSerializer
