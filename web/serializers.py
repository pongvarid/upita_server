from rest_framework.serializers import ModelSerializer
from web.models import WebSetting


class WebSettingSerializer(ModelSerializer):

    class Meta:
        model = WebSetting
        fields = '__all__'
