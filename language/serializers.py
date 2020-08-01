from rest_framework import serializers
from models_app.models import LanguageModel


class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        fields = "__all__"

