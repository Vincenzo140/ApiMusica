from rest_framework import serializers
from API_MUSIC.models.EspInfoEntity import EspInfoEntity

class EspInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspInfoEntity
        fields = '__all__' 