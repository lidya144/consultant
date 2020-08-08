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
    # choice_unit = QuizeChoiceQuestionModel()
    unit_instruction = MatchingInstructionSerializers(many=True, read_only=True)
    unit_choice = ChoiceQuestionSerializers(many=True, read_only=True)
    unit_blank = BlankQuestionSerializers(many=True, read_only=True)
    unit_describe = DescribeQuestionSerializers(many=True, read_only=True)

    class Meta:
        model = UnitModel
        fields = "__all__"

