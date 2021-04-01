from rest_framework.viewsets import ModelViewSet
from oit.serializers import EvaluateOITSerializer
from oit.models import EvaluateOIT
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

class EvaluateOITViewSet(ModelViewSet):
    queryset = EvaluateOIT.objects.order_by('pk')
    serializer_class = EvaluateOITSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['rate', 'rate__year','agency','rate_status']
    search_fields = ['rate__name','agency__name']
