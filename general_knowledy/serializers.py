from rest_framework import serializers
from models_app.models import (
    G_ChoiceQuestionModel,
    G_Options,
    G_UnitModel,
    GeneralKnowlegdyModel,
)


class GeneralKnowledySerializers(serializers.ModelSerializer):
    class Meta:
        model = GeneralKnowlegdyModel
        fields = "__all__"


class G_ChoiceQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = G_ChoiceQuestionModel
        fields = "__all__"


class G_OptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = G_Options
        fields = "__all__"


class G_UnitSerializers(serializers.ModelSerializer):
    class Meta:
        model = G_UnitModel
        fields = "__all__"
