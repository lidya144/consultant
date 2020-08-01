from rest_framework import serializers
from models_app.models import (
    QuizeChoiceQuestionModel,
    QuizeBlankSpaceQuestionModel,
    QuizeDescribeQuestionModel,
    QuizeMatchQuestionModel,
)

# from subject.serializers import SubjectSerializers


class ChoiceQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizeChoiceQuestionModel
        fields = "__all__"


class BlankQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizeBlankSpaceQuestionModel
        fields = "__all__"


class DescribeQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizeDescribeQuestionModel
        fields = "__all__"


class MatchQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizeMatchQuestionModel
        fields = "__all__"
