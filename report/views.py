from rest_framework.viewsets import ModelViewSet
from report.serializers import ReportAllSerializer, ReportDetailSerializer, ReportRawIITSerializer, \
    ReportRawEITSerializer, ReportAllSerializerAll, ReportDetailSerializerAll
from report.models import ReportAll, ReportDetail, ReportRawIIT, ReportRawEIT
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class ReportAllViewSet(ModelViewSet):
    queryset = ReportAll.objects.order_by('pk')
    serializer_class = ReportAllSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency', 'year','rate']
    search_fields = ['agency','year','rate']

class ReportAllViewSetAll(ModelViewSet):
    queryset = ReportAll.objects.order_by('pk')
    serializer_class = ReportAllSerializerAll
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency', 'year','rate']
    search_fields = ['agency','year','rate']

class ReportDetailViewSet(ModelViewSet):
    queryset = ReportDetail.objects.order_by('pk')
    serializer_class = ReportDetailSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency', 'year','name']
    search_fields = ['agency', 'year', 'name']

class ReportDetailViewSetAll(ModelViewSet):
    queryset = ReportDetail.objects.order_by('pk')
    serializer_class = ReportDetailSerializerAll
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency', 'year','name']
    search_fields = ['agency', 'year', 'name']

class ReportRawIITViewSet(ModelViewSet):
    queryset = ReportRawIIT.objects.order_by('pk')
    serializer_class = ReportRawIITSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency', 'year']
    search_fields = ['agency', 'year']


class ReportRawEITViewSet(ModelViewSet):
    queryset = ReportRawEIT.objects.order_by('pk')
    serializer_class = ReportRawEITSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency', 'year']
    search_fields = ['agency', 'year']
