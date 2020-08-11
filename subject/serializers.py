from rest_framework import serializers
from models_app.models import SubjectModel
from unit.serializers import UnitSerializers

from category.serializers import CategorySerializers
from exam.serializers import (
    ChoiceQuestionSerializers,
    MatchingInstructionSerializers,
    BlankQuestionSerializers,
    DescribeQuestionSerializers,
)


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = "__all__"

