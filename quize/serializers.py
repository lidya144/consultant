from rest_framework import serializers
from models_app.models import (
    QuizeChoiceQuestionModel,
    QuizeBlankSpaceQuestionModel,
    QuizeDescribeQuestionModel,
    QuizeMatchingInstructionModel,
    QuizeMatchingPosibleAnswersModels,
    QuizeMatchingQuestionModel,
)


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


class MatchingPosibleAnswersSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizeMatchingPosibleAnswersModels
        fields = "__all__"


class MatchingQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizeMatchingQuestionModel
        fields = "__all__"


class MatchingInstructionSerializers(serializers.ModelSerializer):
    quize_instruction_question = MatchingQuestionSerializers(many=True, read_only=True)
    quize_instruction_posible = MatchingPosibleAnswersSerializers(
        many=True, read_only=True
    )

    class Meta:
        model = QuizeMatchingInstructionModel
        fields = "__all__"

