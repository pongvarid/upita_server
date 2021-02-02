from rest_framework.viewsets import ModelViewSet
from ita.serializers import AgencyTypeSerializer, AgencySerializer, YearSerializer, RateSerializer, RateStatusSerializer, RateResultSerializer, ProfileSerializer
from ita.models import AgencyType, Agency, Year, Rate, RateStatus, RateResult, Profile
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class AgencyTypeViewSet(ModelViewSet):
    queryset = AgencyType.objects.order_by('pk')
    serializer_class = AgencyTypeSerializer


class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.order_by('pk')
    serializer_class = AgencySerializer


class YearViewSet(ModelViewSet):
    queryset = Year.objects.order_by('pk')
    serializer_class = YearSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['status', 'year']
    search_fields = ['year']


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.order_by('pk')
    serializer_class = RateSerializer


class RateStatusViewSet(ModelViewSet):
    queryset = RateStatus.objects.order_by('pk')
    serializer_class = RateStatusSerializer


class RateResultViewSet(ModelViewSet):
    queryset = RateResult.objects.order_by('pk')
    serializer_class = RateResultSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.order_by('pk')
    serializer_class = ProfileSerializer
