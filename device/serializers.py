from rest_framework import serializers
from models_app.models import DeviceModel


class DeviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = "__all__"

