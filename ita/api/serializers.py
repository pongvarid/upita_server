from rest_framework.serializers import ModelSerializer,ValidationError,CharField
from ita.models import AgencyType, Agency, Year, Rate, RateStatus, RateResult, Profile
from django.contrib.auth.models import User



class UserCreateSerializer(ModelSerializer):
    password =  CharField(style={'input_type': 'password'}, write_only=True)
    password2 =  CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise  ValidationError({'password': 'Passwords must match.'})
        user = User(**validated_data)
        user.set_password(password) 
        user.save()
        return user

class AgencyTypeSerializer(ModelSerializer):

    class Meta:
        model = AgencyType
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
