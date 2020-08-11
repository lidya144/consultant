from rest_framework import serializers
from models_app.models import (
    ExamChoiceQuestionModel,
    ExamBlankSpaceQuestionModel,
    ExamDescribeQuestionModel,
    Options,
    MatchingInstructionModel,
    MatchingPosibleAnswersModels,
    MatchingQuestionModel,
)


class MatchingPosibleAnswersSerializers(serializers.ModelSerializer):
    class Meta:
        model = MatchingPosibleAnswersModels
        fields = "__all__"


class MatchingQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = MatchingQuestionModel
        fields = "__all__"


class MatchingInstructionSerializers(serializers.ModelSerializer):
    instruction_question = MatchingQuestionSerializers(many=True, read_only=True)
    instruction_posible = MatchingPosibleAnswersSerializers(many=True, read_only=True)
    question_answers = MatchingPosibleAnswersSerializers(many=True, read_only=True)

    class Meta:
        model = MatchingInstructionModel
        fields = "__all__"


class OptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = "__all__"


class ChoiceQuestionSerializers(serializers.ModelSerializer):
    exam_option = OptionSerializers(many=True, read_only=True)

    class Meta:
        model = ExamChoiceQuestionModel
        fields = "__all__"


class BlankQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExamBlankSpaceQuestionModel
        fields = "__all__"


class DescribeQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExamDescribeQuestionModel
        fields = "__all__"

