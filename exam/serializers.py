from rest_framework import serializers
from models_app.models import (
    ExamChoiceQuestionModel,
    ExamBlankSpaceQuestionModel,
    ExamDescribeQuestionModel,
    ExamMatchQuestionModel,
)

# from subject.serializers import SubjectSerializers


class ChoiceQuestionSerializers(serializers.ModelSerializer):
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


class MatchQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExamMatchQuestionModel
        fields = "__all__"
