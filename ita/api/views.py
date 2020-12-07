from rest_framework.viewsets import ModelViewSet
from ita.api.serializers import AgencyTypeSerializer, AgencySerializer, YearSerializer, RateSerializer, RateStatusSerializer, RateResultSerializer, ProfileSerializer,UserCreateSerializer
from ita.models import AgencyType, Agency, Year, Rate, RateStatus, RateResult, Profile
from django.contrib.auth.models import User
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes


class UserCreate(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class AgencyTypeViewSet(ModelViewSet):
    queryset = AgencyType.objects.order_by('pk')
    serializer_class = AgencyTypeSerializer


class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.order_by('pk')
    serializer_class = AgencySerializer
    # filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    # filterset_fields = ['agency_type__id',]

@permission_classes((AllowAny, ))
class AgencyList(generics.ListAPIView):
    queryset = Agency.objects.all() 
    serializer_class = AgencySerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ['agency_type',]
    search_fields = ['name',]

class YearViewSet(ModelViewSet):
    queryset = Year.objects.order_by('pk')
    serializer_class = YearSerializer


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.order_by('pk')
    serializer_class = RateSerializer


class RateStatusViewSet(ModelViewSet):
    queryset = RateStatus.objects.order_by('pk')
    serializer_class = RateStatusSerializer


class RateResultViewSet(ModelViewSet):
    queryset = RateResult.objects.order_by('pk')
    serializer_class = RateResultSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['rate__year','agency'] 


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.order_by('pk')
    serializer_class = ProfileSerializer
