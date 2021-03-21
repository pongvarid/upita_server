from rest_framework.viewsets import ModelViewSet
from ita.api.serializers import AgencyTypeSerializer, AgencySerializer, YearSerializer, RateSerializer, \
    RateStatusSerializer, RateResultSerializer, ProfileSerializer, UserCreateSerializer, UrlInRateSerializer, \
    RateStatusSerializerAll, ReportAgencyEitSerializerAll, AgencyChangeSerializerAll
from ita.models import AgencyType, Agency, Year, Rate, RateStatus, RateResult, Profile, UrlInRate, ReportAgencyEit, \
    AgencyChange
from django.contrib.auth.models import User
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes


class UrlInRateViewSet(ModelViewSet):
    queryset = UrlInRate.objects.order_by('pk')
    serializer_class = UrlInRateSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ['rateresult',]

class UserCreate(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class AgencyTypeViewSet(ModelViewSet):
    queryset = AgencyType.objects.order_by('pk')
    serializer_class = AgencyTypeSerializer


class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.filter(disabled=False).order_by('name')
    serializer_class = AgencySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency_type', "name", ]
    search_fields = ['name', ]
    # filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    # filterset_fields = ['agency_type__id',]

@permission_classes((AllowAny, ))
class AgencyList(generics.ListAPIView):
    queryset = Agency.objects.filter(disabled=False).order_by('name').all()
    serializer_class = AgencySerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ['agency_type',]
    search_fields = ['name',]

class AgencyListLog(ModelViewSet):
    queryset = AgencyChange.objects.order_by('pk')
    serializer_class = AgencyChangeSerializerAll
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['agency','agency_change', 'user']


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

class RateStatusViewSetAll(ModelViewSet):
    queryset = RateStatus.objects.order_by('pk')
    serializer_class = RateStatusSerializerAll

class RateResultViewSet(ModelViewSet):
    queryset = RateResult.objects.order_by('pk')
    serializer_class = RateResultSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['rate__year','agency','rate']


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.order_by('pk')
    serializer_class = ProfileSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['user',]

class ReportAgencyEitViewSet(ModelViewSet):
    queryset = ReportAgencyEit.objects.order_by('pk')
    serializer_class = ReportAgencyEitSerializerAll
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['agency', 'year']

