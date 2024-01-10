from rest_framework.serializers import ModelSerializer, SerializerMethodField
from oit.models import EvaluateOIT


class EvaluateOITSerializer(ModelSerializer):
    rate_no = SerializerMethodField(read_only=True)
    rate_type = SerializerMethodField(read_only=True) 
    class Meta:
        model = EvaluateOIT
        fields = '__all__'
    
    def get_rate_no(self,obj):
        try:
            return obj.rate.number
        except:
            return None 
    def get_rate_type(self,obj): 
        try:
            return obj.rate.type_base
        except:
            return None
