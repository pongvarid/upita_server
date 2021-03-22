from rest_framework.serializers import ModelSerializer
from oit.models import EvaluateOIT


class EvaluateOITSerializer(ModelSerializer):

    class Meta:
        model = EvaluateOIT
        fields = '__all__'
