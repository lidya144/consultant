from rest_framework import serializers
from models_app.models import CategoryModel
from unit.serializers import UnitSerializers
from exam.serializers import (
    ChoiceQuestionSerializers,
    MatchingInstructionSerializers,
    BlankQuestionSerializers,
    DescribeQuestionSerializers,
)


class CategorySerializers(serializers.ModelSerializer):
    category_unit = UnitSerializers(many=True, read_only=True)
    category_choice = ChoiceQuestionSerializers(many=True, read_only=True)
    category_instruction = MatchingInstructionSerializers(many=True, read_only=True)
    category_blank = BlankQuestionSerializers(many=True, read_only=True)
    category_describe = DescribeQuestionSerializers(many=True, read_only=True)

    class Meta:
        model = CategoryModel
        fields = "__all__"

