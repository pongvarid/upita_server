from rest_framework.serializers import ModelSerializer
from ita.models import AgencyType, Agency, Year, Rate, RateStatus, RateResult, Profile
from django.contrib.auth.models import User


class AgencyTypeSerializer(ModelSerializer):

    class Meta:
        model = AgencyType
        fields = '__all__'

class UserViewSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class AgencySerializer(ModelSerializer):

    class Meta:
        model = Agency
        fields = '__all__'


class YearSerializer(ModelSerializer):

    class Meta:
        model = Year
        fields = '__all__'


class RateSerializer(ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'


class RateStatusSerializer(ModelSerializer):

    class Meta:
        model = RateStatus
        fields = '__all__'


class RateResultSerializer(ModelSerializer):

    class Meta:
        model = RateResult
        fields = '__all__'


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
