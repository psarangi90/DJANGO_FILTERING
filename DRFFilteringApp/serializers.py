from rest_framework.serializers import ModelSerializer
from .models import WFMTModel
class WFMTModelSerializer(ModelSerializer):
    class Meta:
        model=WFMTModel
        fields="__all__"