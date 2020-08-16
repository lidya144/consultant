from rest_framework import serializers
from models_app.models import Contactinfo


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactinfo
        fields = "__all__"

