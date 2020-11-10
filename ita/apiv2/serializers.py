from rest_framework.serializers import ModelSerializer,Field,SerializerMethodField
from ita.models import AgencyType, Agency, Year, Rate, RateStatus, RateResult, Profile
from django.contrib.auth import get_user_model, authenticate
UserModel = get_user_model()

class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class UserDetailsSerializer(ModelSerializer):
    """
    User model w/o password
    """
    ext_link = SerializerMethodField()
    status = SerializerMethodField()
    register_type = SerializerMethodField()
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'first_name', 'last_name','is_superuser','is_staff','is_active','ext_link','status','register_type')
        read_only_fields = ('email', )

    def get_ext_link(self, obj):
        try:
            profile = Profile.objects.get(user_id=obj.pk)
            data = ProfileSerializer(profile)
            return data.data
        except:
            return None
        
    def get_status(self, obj):
        try:
            profile = Profile.objects.get(user_id=obj.pk) 
            return profile.status
        except:
            return None 

    def get_register_type(self, obj):
        try:
            profile = Profile.objects.get(user_id=obj.pk) 
            return profile.register_type
        except:
            return None 

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


