from rest_framework import serializers
from models_app.models import UnitModel
from utilities.image_validation import validate_image
from quize.serializers import (
    QuizeChoiceQuestionModel,
    MatchingInstructionSerializers,
    ChoiceQuestionSerializers,
    BlankQuestionSerializers,
    DescribeQuestionSerializers,
)


class UnitSerializers(serializers.ModelSerializer):
    class Meta:
        model = UnitModel
        fields = "__all__"

