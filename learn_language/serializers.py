from rest_framework import serializers
from models_app.models import (
    LearnLanguageModel,
    L_ChoiceQuestionModel,
    L_Options,
    L_UnitModel,
)


class LearnLanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = LearnLanguageModel
        fields = "__all__"


class L_ChoiceQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = L_ChoiceQuestionModel
        fields = "__all__"


class L_OptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = L_Options
        fields = "__all__"


class L_UnitSerializers(serializers.ModelSerializer):
    class Meta:
        model = L_UnitModel
        fields = "__all__"
