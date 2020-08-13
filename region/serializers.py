from rest_framework import serializers
from models_app.models import RegionModel


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegionModel
        fields = "__all__"

